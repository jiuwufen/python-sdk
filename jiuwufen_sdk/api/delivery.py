"""
Delivery API
"""

from typing import Any, Dict, Optional, List


class DeliveryApi:
    """Delivery API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    
    def delivery_biz(self, **kwargs) -> Dict[str, Any]:
        """
        发货 & 重打面单
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/delivery/bizDelivery/v1.0", kwargs)
