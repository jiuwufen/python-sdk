"""
Product API
"""

from typing import Any, Dict, Optional, List


class ProductApi:
    """Product API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    def sku_list_binding(self, merchant_sku_code: Optional[list] = None, start_binding_time: Optional[str] = None, end_binding_time: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
        """
        定时拉取绑定关系,查询绑定关系,至少时间范围要拉取前一天的。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'merchant_sku_code': merchant_sku_code, 'start_binding_time': start_binding_time, 'end_binding_time': end_binding_time, 'page': page, 'page_size': page_size}.items() if v is not None}
        return self.client.request("/api_tob/merchantSkuList/v1.0", params_dict)

    def sku_list_general(self, child_category_id_list: list, page: Optional[int] = None, page_size: Optional[int] = None, brand_name: Optional[str] = None, brand_id: Optional[int] = None, title: Optional[str] = None, code: Optional[str] = None, spu_id: Optional[int] = None, last_id: Optional[int] = None, ids: Optional[list] = None, must_status: Optional[int] = None) -> Dict[str, Any]:
        """
        通用查询,不限制商品绑定。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'child_category_id_list': child_category_id_list, 'page': page, 'page_size': page_size, 'brand_name': brand_name, 'brand_id': brand_id, 'title': title, 'code': code, 'spu_id': spu_id, 'last_id': last_id, 'ids': ids, 'must_status': must_status}.items() if v is not None}
        return self.client.request("/api_tob/skuList/v1.0", params_dict)

    def add_order_goods(self, goods_sn: str, brand_id: int, l1_category_id: int, first_img: str, general_imgs: list, price: int, title: Optional[str] = None, l2_category_id: Optional[int] = None, quality: Optional[int] = None, size: Optional[str] = None, parts: Optional[str] = None, code: Optional[str] = None, remark: Optional[str] = None, flaw_desc: Optional[str] = None, flaw_imgs: Optional[list] = None, fit_id: Optional[int] = None, support_bargain: Optional[int] = None, property_list: Optional[list] = None) -> Dict[str, Any]:
        """
        新增商品接口。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'brand_id': brand_id, 'l1_category_id': l1_category_id, 'first_img': first_img, 'general_imgs': general_imgs, 'price': price, 'title': title, 'l2_category_id': l2_category_id, 'quality': quality, 'size': size, 'parts': parts, 'code': code, 'remark': remark, 'flaw_desc': flaw_desc, 'flaw_imgs': flaw_imgs, 'fit_id': fit_id, 'support_bargain': support_bargain, 'property_list': property_list}.items() if v is not None}
        return self.client.request("/api_tob/addOrderGoods/v1.0", params_dict)

    def goods_info(self, goods_sn: str) -> Dict[str, Any]:
        """
        查询商品的上架状态及详情链接。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn}.items() if v is not None}
        return self.client.request("/api_tob/goodsInfo/v1.0", params_dict)

    def update_price(self, goods_sn: str, price: int) -> Dict[str, Any]:
        """
        改价
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'price': price}.items() if v is not None}
        return self.client.request("/api_tob/updatePrice/v1.0", params_dict)

    def cancel_order(self, goods_sn: str, type: Optional[int] = None) -> Dict[str, Any]:
        """
        下架商品
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'type': type}.items() if v is not None}
        return self.client.request("/api_tob/cancelOrder/v1.0", params_dict)

    def update_seller_bargain(self, goods_sn: str, price: int) -> Dict[str, Any]:
        """
        卖家议价 (UpdateSellerBargain)
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'price': price}.items() if v is not None}
        return self.client.request("/api_tob/updateSellerBargain/v1.0", params_dict)

    def bargain_success(self, goods_sn: str, price: int) -> Dict[str, Any]:
        """
        卖家接受还价 (BargainSuccess)
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'price': price}.items() if v is not None}
        return self.client.request("/api_tob/bargainSuccess/v1.0", params_dict)

    def query_properties(self, child_category_id: int) -> Dict[str, Any]:
        """
        通过叶子类目 ID 获取 95 分该类目下具体的销售属性列表。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'child_category_id': child_category_id}.items() if v is not None}
        return self.client.request("/api_tob/query_properties/v1.0", params_dict)

    def get_brand_identify_ability(self, l1_category_id: int, brand_name: str, l2_category_id: Optional[int] = None) -> Dict[str, Any]:
        """
        通过一级类目 ID 和品牌名称获取 95 分可鉴品牌列表,返回前 100 个符合条件的品牌信息。支持模糊查询。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'l1_category_id': l1_category_id, 'brand_name': brand_name, 'l2_category_id': l2_category_id}.items() if v is not None}
        return self.client.request("/api_tob/get_brand_identify_ability/v1.0", params_dict)

    def copy_on_sale(self, old_goods_sn: str, new_goods_sn: str, price: int) -> Dict[str, Any]:
        """
        复制订单上架 (CopyOnSale)
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'old_goods_sn': old_goods_sn, 'new_goods_sn': new_goods_sn, 'price': price}.items() if v is not None}
        return self.client.request("/api_tob/copyOnSale/v1.0", params_dict)

    def reference_price(self, goods_sn: str, order_number: str, sku_id: Optional[int] = None, is_new: Optional[int] = None, sale_type: Optional[int] = None) -> Dict[str, Any]:
        """
        查询参考价格,包含平台最低价、寄售最低价、最近成交均价、全新市场价、平台限价(3C专属,为最高出价限制)。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'order_number': order_number, 'sku_id': sku_id, 'is_new': is_new, 'sale_type': sale_type}.items() if v is not None}
        return self.client.request("/api_tob/referencePrice/v1.0", params_dict)
