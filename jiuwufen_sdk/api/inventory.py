"""
Inventory API
"""

from typing import Any, Dict, Optional, List


class InventoryApi:
    """Inventory API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    
    def sync_inventory(self, detail: list) -> Dict[str, Any]:
        """
        库存同步
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/inventory/sync/v1.0", {'detail': detail})

    
    def get_inventory_list(self, detail: list) -> Dict[str, Any]:
        """
        库存查询
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/inventory/list/v1.0", {'detail': detail})

    
    def update_stock(self, goods_sn: str, stock: int) -> Dict[str, Any]:
        """
        同步库存（上下架）
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/updateStock/v1.0", {'goods_sn': goods_sn, 'stock': stock})
