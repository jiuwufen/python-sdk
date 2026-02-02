"""
Order API
"""

from typing import Any, Dict, Optional, List


class OrderApi:
    """Order API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    
    def get_consign_order_info(self, **kwargs) -> Dict[str, Any]:
        """
        查询商品订单信息
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/consignOrderInfo/v1.0", kwargs)

    
    def get_buyer_address(self, order_number: str) -> Dict[str, Any]:
        """
        买家地址查询
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/order/buyerAddress", {'order_number': order_number})

    
    def get_consign_batch_order_list(self, batch_number: str) -> Dict[str, Any]:
        """
        自送货订单明细查询
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/consignBatchOrderList/v1.0", {'batch_number': batch_number})

    
    def get_order_list(self, **kwargs) -> Dict[str, Any]:
        """
        获取订单列表（挂售）
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/getOrderList/v1.0", kwargs)
