"""
Order API
"""

from typing import Any, Dict, Optional, List


class OrderApi:
    """Order API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    def consign_order_info(self, upc: Optional[str] = None, order_number: Optional[list] = None, batch_number: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None, goods_sn: Optional[str] = None, is_fee_detail: Optional[int] = None, is_retrieve: Optional[int] = None) -> Dict[str, Any]:
        """
        查询商品的寄售订单详情。注意:goods_sn、upc、order_number、batch_number 必传其中一个。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'upc': upc, 'order_number': order_number, 'batch_number': batch_number, 'page': page, 'page_size': page_size, 'goods_sn': goods_sn, 'is_fee_detail': is_fee_detail, 'is_retrieve': is_retrieve}.items() if v is not None}
        return self.client.request("/api_tob/consignOrderInfo/v1.0", params_dict)

    def buyer_address(self, order_number: str) -> Dict[str, Any]:
        """
        获取买家详细收货地址 (加密)。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'order_number': order_number}.items() if v is not None}
        return self.client.request("/api_tob/order/buyerAddress", params_dict)

    def consign_batch_order_list(self, mother_no: str, page: Optional[int] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
        """
        查询自送货批次下的订单明细及查验结果。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'mother_no': mother_no, 'page': page, 'page_size': page_size}.items() if v is not None}
        return self.client.request("/api_tob/consignBatchOrderList/v1.0", params_dict)

    def get_order_list(self, goods_sn_list: list) -> Dict[str, Any]:
        """
        获取挂售订单列表。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn_list': goods_sn_list}.items() if v is not None}
        return self.client.request("/api_tob/getOrderList/v1.0", params_dict)

    def merchant_order_info(self, start_update: Optional[str] = None, end_update: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None, order_number: Optional[list] = None, merchant_sku_code: Optional[str] = None, express_number: Optional[str] = None, is_delivery_late: Optional[bool] = None, is_delivery_timeout_imminent: Optional[bool] = None, is_fee_detail: Optional[int] = None) -> Dict[str, Any]:
        """
        查询直发订单列表。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'start_update': start_update, 'end_update': end_update, 'page': page, 'page_size': page_size, 'order_number': order_number, 'merchant_sku_code': merchant_sku_code, 'express_number': express_number, 'is_delivery_late': is_delivery_late, 'is_delivery_timeout_imminent': is_delivery_timeout_imminent, 'is_fee_detail': is_fee_detail}.items() if v is not None}
        return self.client.request("/api_tob/merchantOrderInfo/v1.0", params_dict)
