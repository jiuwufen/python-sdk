"""
95分开放平台 SDK 客户端
"""

import logging
import time
from typing import Any, Dict, Optional
import requests

from .api.merchant import MerchantApi
from .api.goods import GoodsApi
from .api.inventory import InventoryApi
from .api.order import OrderApi
from .api.delivery import DeliveryApi
from .utils.signature import SignatureUtil
from .exceptions import ApiException

logger = logging.getLogger(__name__)


class JiuWuFenClient:
    """
    95分开放平台 SDK 客户端
    
    使用示例:
        >>> client = JiuWuFenClient(
        ...     erp_name="your-erp-name",
        ...     third_party_id="your-third-party-id",
        ...     merchant_secret="your-merchant-secret",
        ...     platform_secret="your-platform-secret",
        ...     base_url="http://d1.95fenapp.com"
        ... )
        >>> response = client.merchant.send_sms_captcha(mobile="13800000000")
    """
    
    def __init__(
        self,
        erp_name: str,
        third_party_id: str,
        merchant_secret: str,
        platform_secret: str,
        base_url: str = "http://www.95fenapp.com",
        timeout: int = 30,
        debug: bool = False
    ):
        """
        初始化客户端
        
        Args:
            erp_name: ERP 名称（由95分提供）
            third_party_id: 第三方应用标识（由95分提供）
            merchant_secret: 商家密钥（入驻后获取）
            platform_secret: 平台密钥（由95分提供）
            base_url: API 基础 URL
            timeout: 请求超时时间（秒）
            debug: 是否开启调试模式
        """
        if not erp_name:
            raise ValueError("erp_name is required")
        if not third_party_id:
            raise ValueError("third_party_id is required")
        if not merchant_secret:
            raise ValueError("merchant_secret is required")
        if not platform_secret:
            raise ValueError("platform_secret is required")
        
        self.erp_name = erp_name
        self.third_party_id = third_party_id
        self.merchant_secret = merchant_secret
        self.platform_secret = platform_secret
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.debug = debug
        
        # 初始化 HTTP 会话
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json; charset=UTF-8',
            'x-request-sign-version': 'm1',
            'fen95-external-third-erp-name': self.erp_name,
            'fen95-external-third': self.third_party_id,
        })
        
        # 初始化签名工具
        self.signature_util = SignatureUtil(merchant_secret, platform_secret)
        
        # 初始化 API 服务
        self._merchant = MerchantApi(self)
        self._goods = GoodsApi(self)
        self._inventory = InventoryApi(self)
        self._order = OrderApi(self)
        self._delivery = DeliveryApi(self)
    
    @property
    def merchant(self) -> MerchantApi:
        """商户入驻 API"""
        return self._merchant
    
    @property
    def goods(self) -> GoodsApi:
        """商品管理 API"""
        return self._goods
    
    @property
    def inventory(self) -> InventoryApi:
        """库存管理 API"""
        return self._inventory
    
    @property
    def order(self) -> OrderApi:
        """订单管理 API"""
        return self._order
    
    @property
    def delivery(self) -> DeliveryApi:
        """物流管理 API"""
        return self._delivery
    
    def request(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        执行 HTTP 请求
        
        Args:
            path: 请求路径
            data: 请求数据
            
        Returns:
            响应数据
            
        Raises:
            ApiException: API 异常
        """
        if data is None:
            data = {}
        
        # 处理时间戳（如果没有传入，则自动添加当前时间戳，单位：秒）
        if 'timestamp' not in data:
            data['timestamp'] = str(int(time.time()))
        
        # 生成签名
        signature = self.signature_util.generate_signature(data)
        data['token'] = signature
        
        # 构建 URL
        url = f"{self.base_url}{path}"
        
        if self.debug:
            logger.debug(f"Request URL: {url}")
            logger.debug(f"Request Data: {data}")
        
        try:
            # 发送请求
            response = self.session.post(
                url,
                json=data,
                timeout=self.timeout
            )
            
            if self.debug:
                logger.debug(f"Response Status: {response.status_code}")
                logger.debug(f"Response Body: {response.text}")
            
            # 检查 HTTP 状态码
            response.raise_for_status()
            
            # 解析响应
            result = response.json()
            
            # 检查业务状态码
            status = result.get('status', -1)
            if status != 0:
                raise ApiException(
                    code=status,
                    message=result.get('msg', 'Unknown error'),
                    req_id=result.get('req_id', '')
                )
            
            return result.get('data', {})
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
            raise ApiException(
                code=-1,
                message=f"Network error: {str(e)}",
                req_id=''
            )
        except ValueError as e:
            logger.error(f"JSON decode error: {e}")
            raise ApiException(
                code=-1,
                message=f"Invalid JSON response: {str(e)}",
                req_id=''
            )
    
    def close(self):
        """关闭 HTTP 会话"""
        self.session.close()
    
    def __enter__(self):
        """上下文管理器入口"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.close()
