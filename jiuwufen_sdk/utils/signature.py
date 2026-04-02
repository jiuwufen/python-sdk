"""
签名和加解密工具
"""

import base64
import copy
import hashlib
import json
import math
from decimal import Decimal
from typing import Any, Dict
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class SignatureUtil:
    """
    签名工具类
    
    提供签名生成、验证和地址解密功能
    """
    
    def __init__(self, merchant_secret: str, platform_secret: str):
        """
        初始化签名工具
        
        Args:
            merchant_secret: 商家密钥
            platform_secret: 平台密钥
        """
        self.merchant_secret = merchant_secret
        self.platform_secret = platform_secret
    
    def generate_signature(self, params: Dict[str, Any]) -> str:
        """
        生成请求签名
        
        算法: token = md5(base64_encode(商家密钥 + 平台密钥) + 排序并拼接后的参数字符串)
        与 Java SignatureUtil / GenSign 一致：仅 str 原样拼接，其余 json.dumps（含 None→null）；
        嵌套 dict 先排序 key；整型语义的 float 先归一为 int（对齐 Go json / Java Gson）。
        
        Args:
            params: 请求参数
            
        Returns:
            签名字符串
        """
        work = self._normalize_integral(copy.deepcopy(params))

        # 1. 获取所有 Keys 并排序（排除 token 本身）
        keys = sorted([k for k in work.keys() if k != 'token'])

        # 2. 拼接参数值
        params_str = ""
        for key in keys:
            value = work[key]
            if isinstance(value, str):
                params_str += value
            else:
                params_str += json.dumps(
                    self._sort_dict_keys(value),
                    ensure_ascii=False,
                    separators=(',', ':'),
                )
        
        # 3. Base64 编码密钥
        secret = self.merchant_secret + self.platform_secret
        base64_secret = base64.b64encode(secret.encode('utf-8')).decode('utf-8')
        
        # 4. 拼接并计算 MD5
        final_str = base64_secret + params_str
        return hashlib.md5(final_str.encode('utf-8')).hexdigest()

    def _normalize_integral(self, obj: Any) -> Any:
        """递归将整型语义的 float 转为 int，与 Java/Golang 侧 JSON 数字形态对齐。"""
        if obj is None:
            return None
        if isinstance(obj, dict):
            return {k: self._normalize_integral(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [self._normalize_integral(x) for x in obj]
        if isinstance(obj, float) and math.isfinite(obj) and obj.is_integer():
            iv = int(obj)
            if -(2 ** 63) <= iv <= 2 ** 63 - 1:
                return iv
            return obj
        if isinstance(obj, Decimal):
            try:
                if obj == obj.to_integral_value():
                    return int(obj)
            except (OverflowError, ValueError, ArithmeticError):
                pass
            return obj
        return obj
    
    def verify_signature(self, params: Dict[str, Any], expected_token: str) -> bool:
        """
        验证签名
        
        Args:
            params: 请求参数
            expected_token: 期望的签名
            
        Returns:
            是否验证通过
        """
        actual_token = self.generate_signature(params)
        return actual_token == expected_token
    
    @staticmethod
    def decrypt_address(cipher_text: str, key: bytes) -> str:
        """
        解密地址
        
        使用 AES-ECB 模式解密地址字符串
        
        Args:
            cipher_text: 密文（Base64 编码）
            key: 密钥
            
        Returns:
            明文地址
        """
        # Base64 解码密文
        cipher_bytes = base64.b64decode(cipher_text)
        
        # 创建 AES cipher
        cipher = AES.new(key, AES.MODE_ECB)
        
        # 解密
        plain_bytes = cipher.decrypt(cipher_bytes)
        
        # 去除 PKCS7 填充
        plain_bytes = unpad(plain_bytes, AES.block_size)
        
        return plain_bytes.decode('utf-8')
    
    @staticmethod
    def encrypt_address(plain_text: str, key: bytes) -> str:
        """
        加密地址（用于测试）
        
        Args:
            plain_text: 明文
            key: 密钥
            
        Returns:
            密文（Base64 编码）
        """
        # 创建 AES cipher
        cipher = AES.new(key, AES.MODE_ECB)
        
        # PKCS7 填充
        plain_bytes = pad(plain_text.encode('utf-8'), AES.block_size)
        
        # 加密
        cipher_bytes = cipher.encrypt(plain_bytes)
        
        # Base64 编码
        return base64.b64encode(cipher_bytes).decode('utf-8')
    
    def _sort_dict_keys(self, obj: Any) -> Any:
        """
        递归排序字典的 Keys
        
        Args:
            obj: 要排序的对象
            
        Returns:
            排序后的对象
        """
        if isinstance(obj, dict):
            return {k: self._sort_dict_keys(v) for k, v in sorted(obj.items())}
        if isinstance(obj, list):
            return [self._sort_dict_keys(item) for item in obj]
        return obj
