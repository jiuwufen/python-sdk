"""
Goods API
"""

from typing import Any, Dict, Optional, List


class GoodsApi:
    """Goods API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    
    def get_merchant_sku_list(self, **kwargs) -> Dict[str, Any]:
        """
        查询SKU列表（绑定关系）
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/merchantSkuList/v1.0", kwargs)

    
    def add_order_goods(self, **kwargs) -> Dict[str, Any]:
        """
        新增商品
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/addOrderGoods/v1.0", kwargs)

    
    def get_goods_info(self, goods_sn: str) -> Dict[str, Any]:
        """
        查询商品状态信息
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/goodsInfo/v1.0", {'goods_sn': goods_sn})

    
    def update_price(self, goods_sn: str, price: int) -> Dict[str, Any]:
        """
        改价
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/updatePrice/v1.0", {'goods_sn': goods_sn, 'price': price})

    
    def cancel_order(self, goods_sn: str) -> Dict[str, Any]:
        """
        下架商品
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/cancelOrder/v1.0", {'goods_sn': goods_sn})

    
    def update_seller_bargain(self, goods_sn: str, price: int) -> Dict[str, Any]:
        """
        卖家议价
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/updateSellerBargain/v1.0", {'goods_sn': goods_sn, 'price': price})

    
    def bargain_success(self, goods_sn: str) -> Dict[str, Any]:
        """
        卖家接受还价
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/bargainSuccess/v1.0", {'goods_sn': goods_sn})

    
    def query_properties(self, child_category_id: int) -> Dict[str, Any]:
        """
        获取类目属性
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/query_properties/v1.0", {'child_category_id': child_category_id})

    
    def get_brand_identify_ability(self, l1_category_id: int, brand_name: str) -> Dict[str, Any]:
        """
        可鉴品牌查询
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/get_brand_identify_ability/v1.0", {'l1_category_id': l1_category_id, 'brand_name': brand_name})

    
    def copy_on_sale(self, goods_sn: str) -> Dict[str, Any]:
        """
        复制订单上架
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/copyOnSale/v1.0", {'goods_sn': goods_sn})

    
    def get_reference_price(self, goods_sn: str) -> Dict[str, Any]:
        """
        订单参考价查询
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/referencePrice/v1.0", {'goods_sn': goods_sn})
