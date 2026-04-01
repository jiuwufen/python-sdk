"""
Logistics API
"""

from typing import Any, Dict, Optional, List


class LogisticsApi:
    """Logistics API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    def delivery_biz(self, order_number: str, send_address: Any) -> Dict[str, Any]:
        """
        商家发货并获取面单信息。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'order_number': order_number, 'send_address': send_address}.items() if v is not None}
        return self.client.request("/api_tob/delivery/bizDelivery/v1.0", params_dict)

    def consign_platform_delivery(self, goods_sn: str, internal_enterprise_id: Optional[str] = None, imei: Optional[str] = None, address: Optional[dict] = None) -> Dict[str, Any]:
        """
        寄售模式下,商家申请打印面单并发货。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'internal_enterprise_id': internal_enterprise_id, 'imei': imei, 'address': address}.items() if v is not None}
        return self.client.request("/api_tob/platformDeliver/v1.0", params_dict)

    def save_express_number(self, goods_sn: str, express_number: str, express_type: int, address: Optional[dict] = None) -> Dict[str, Any]:
        """
        发货到平台 (SaveExpressNumber)
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'express_number': express_number, 'express_type': express_type, 'address': address}.items() if v is not None}
        return self.client.request("/api_tob/saveExpressNumber/v1.0", params_dict)

    def inspect_logistics_query(self, goods_sn_arr: list, delivery_method: int, express_number: Optional[str] = None, express_type: Optional[int] = None, internal_enterprise_id: Optional[str] = None, address: Optional[dict] = None) -> Dict[str, Any]:
        """
        后验模式下,商家申请打印面单并发货。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn_arr': goods_sn_arr, 'delivery_method': delivery_method, 'express_number': express_number, 'express_type': express_type, 'internal_enterprise_id': internal_enterprise_id, 'address': address}.items() if v is not None}
        return self.client.request("/api_tob/inspectLogisticsQuery/v1.0", params_dict)

    def post_verification_warehouse_info(self, rule_id: int) -> Dict[str, Any]:
        """
        查询后验仓地址信息。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'rule_id': rule_id}.items() if v is not None}
        return self.client.request("/api_tob/postVerificationWarehouseInfo/v1.0", params_dict)

    def delivery_confirm(self, order_number: str, express_number: str, address: Optional[Any] = None) -> Dict[str, Any]:
        """
        确认发货完成。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'order_number': order_number, 'express_number': express_number, 'address': address}.items() if v is not None}
        return self.client.request("/api_tob/delivery/confirm/v1.0", params_dict)

    def logistics_query(self, express_number: str, is_reverse: Optional[bool] = None) -> Dict[str, Any]:
        """
        查询运单物流轨迹。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'express_number': express_number, 'is_reverse': is_reverse}.items() if v is not None}
        return self.client.request("/api_tob/logisticsQuery/v1.0", params_dict)
