"""
签名工具测试
"""

import unittest
from jiuwufen_sdk.utils.signature import SignatureUtil


class TestSignatureUtil(unittest.TestCase):
    """签名工具测试类"""
    
    def setUp(self):
        """测试前准备"""
        self.merchant_secret = "merchant_secret_123"
        self.platform_secret = "platform_secret_456"
        self.util = SignatureUtil(self.merchant_secret, self.platform_secret)
    
    def test_generate_signature(self):
        """测试签名生成"""
        params = {"mobile": "13800000000"}
        signature = self.util.generate_signature(params)
        
        self.assertIsNotNone(signature)
        self.assertEqual(len(signature), 32)  # MD5 长度为 32
    
    def test_generate_signature_with_multiple_params(self):
        """测试多参数签名生成"""
        params = {
            "b": "2",
            "a": "1",
            "c": "3"
        }
        signature = self.util.generate_signature(params)
        
        self.assertIsNotNone(signature)
        self.assertEqual(len(signature), 32)
    
    def test_verify_signature(self):
        """测试签名验证"""
        params = {"mobile": "13800000000"}
        
        # 生成签名
        signature = self.util.generate_signature(params)
        
        # 验证签名
        self.assertTrue(self.util.verify_signature(params, signature))
        
        # 验证错误的签名
        self.assertFalse(self.util.verify_signature(params, "invalid_signature"))
    
    def test_encrypt_decrypt_address(self):
        """测试地址加解密"""
        plain_text = "上海市浦东新区张江高科技园区"
        key = b"12345678901234567890123456789012"  # 32字节密钥
        
        # 加密
        cipher_text = SignatureUtil.encrypt_address(plain_text, key)
        self.assertIsNotNone(cipher_text)
        self.assertGreater(len(cipher_text), 0)
        
        # 解密
        decrypted = SignatureUtil.decrypt_address(cipher_text, key)
        self.assertEqual(decrypted, plain_text)
    
    def test_signature_consistency(self):
        """测试签名一致性"""
        params = {
            "goods_sn": "GOODS-001",
            "price": 29900
        }
        
        signature1 = self.util.generate_signature(params)
        signature2 = self.util.generate_signature(params)
        
        # 相同参数应该生成相同的签名
        self.assertEqual(signature1, signature2)

if __name__ == "__main__":
    unittest.main()
