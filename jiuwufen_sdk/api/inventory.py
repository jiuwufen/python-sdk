"""
Inventory API
"""

from typing import Any, Dict, Optional, List


class InventoryApi:
    """Inventory API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    def inventory_sync(self, detail: list) -> Dict[str, Any]:
        """
        95 分平台的库存变更,三方要保证 95 分库存售出操作了发货确认后实时同步总库存的变更。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'detail': detail}.items() if v is not None}
        return self.client.request("/api_tob/inventory/sync/v1.0", params_dict)

    def inventory_list(self, detail: list) -> Dict[str, Any]:
        """
        查询当前库存状态。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'detail': detail}.items() if v is not None}
        return self.client.request("/api_tob/inventory/list/v1.0", params_dict)

    def update_stock(self, goods_sn: str, stock: int) -> Dict[str, Any]:
        """
        同步库存 (UpdateStock)
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'stock': stock}.items() if v is not None}
        return self.client.request("/api_tob/updateStock/v1.0", params_dict)
