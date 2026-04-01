"""
Return API
"""

from typing import Any, Dict, Optional, List


class ReturnApi:
    """Return API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    def refund_list(self, seller_order_number: Optional[str] = None, refund_number: Optional[str] = None, in_express_number: Optional[str] = None, refund_step: Optional[int] = None, apply_time_start: Optional[str] = None, apply_time_end: Optional[str] = None, last_update_start: Optional[str] = None, last_update_end: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
        """
        查询退货订单列表。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'seller_order_number': seller_order_number, 'refund_number': refund_number, 'in_express_number': in_express_number, 'refund_step': refund_step, 'apply_time_start': apply_time_start, 'apply_time_end': apply_time_end, 'last_update_start': last_update_start, 'last_update_end': last_update_end, 'page': page, 'page_size': page_size}.items() if v is not None}
        return self.client.request("/api_tob/refund/list/v1.0", params_dict)

    def refund_confirm(self, refund_number: str) -> Dict[str, Any]:
        """
        商家确认签收退货。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'refund_number': refund_number}.items() if v is not None}
        return self.client.request("/api_tob/refund/confirmReceive", params_dict)

    def refund_buyer_address(self, refund_number: str) -> Dict[str, Any]:
        """
        查询买家退回的地址 (加密)。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'refund_number': refund_number}.items() if v is not None}
        return self.client.request("/api_tob/refund/backBuyerAddress", params_dict)

    def refund_success(self, refund_number: str, return_express_number: str, return_express_type: int) -> Dict[str, Any]:
        """
        退货审核不通过时,发货退回给买家。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'refund_number': refund_number, 'return_express_number': return_express_number, 'return_express_type': return_express_type}.items() if v is not None}
        return self.client.request("/api_tob/refund/refundSuccess", params_dict)

    def refund_order_info(self, refund_time: Optional[str] = None, goods_sn: Optional[str] = None, order_number: Optional[list] = None, page: Optional[int] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
        """
        查询退货订单列表详情。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'refund_time': refund_time, 'goods_sn': goods_sn, 'order_number': order_number, 'page': page, 'page_size': page_size}.items() if v is not None}
        return self.client.request("/api_tob/refundOrderInfo/v1.0", params_dict)
