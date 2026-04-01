"""
DigitalProduct API
"""

from typing import Any, Dict, Optional, List


class DigitalProductApi:
    """DigitalProduct API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    def examining_config(self, template_id: int) -> Dict[str, Any]:
        """
        查询 3C 数码产品的质检项配置。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'template_id': template_id}.items() if v is not None}
        return self.client.request("/api_tob/examiningConfig/v1.0", params_dict)

    def imei_query(self, imei: str) -> Dict[str, Any]:
        """
        查询设备 IMEI 上架状态。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'imei': imei}.items() if v is not None}
        return self.client.request("/api_tob/imei/v1.0", params_dict)

    def digital_super_sale(self, goods_sn: str, sku_id: int, quality: int, address: dict, imei: str, price: int, general_imgs: list, examining_list: list, result_desc: str, template_id: int, flaw_imgs: Optional[list] = None, internal_enterprise_id: Optional[str] = None, product_source_type: Optional[int] = None) -> Dict[str, Any]:
        """
        平台商家一键出售 3C 数码商品。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'sku_id': sku_id, 'quality': quality, 'address': address, 'imei': imei, 'price': price, 'general_imgs': general_imgs, 'examining_list': examining_list, 'result_desc': result_desc, 'template_id': template_id, 'flaw_imgs': flaw_imgs, 'internal_enterprise_id': internal_enterprise_id, 'product_source_type': product_source_type}.items() if v is not None}
        return self.client.request("/api_tob/digitalSuperSale/v1.0", params_dict)

    def digital_super_sale_v2(self, goods_sn: str, sku_id: int, quality: str, address: dict, imei: str, price: int, general_imgs: list, examining_list: list, result_desc: str, flaw_imgs: Optional[list] = None) -> Dict[str, Any]:
        """
        自研商家一键出售 3C 数码商品 (V2 版本)。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'goods_sn': goods_sn, 'sku_id': sku_id, 'quality': quality, 'address': address, 'imei': imei, 'price': price, 'general_imgs': general_imgs, 'examining_list': examining_list, 'result_desc': result_desc, 'flaw_imgs': flaw_imgs}.items() if v is not None}
        return self.client.request("/api_tob/digitalSuperSale/v2.0", params_dict)

    def inspect_sign_receipt(self, express_number: str) -> Dict[str, Any]:
        """
        商家确认签收后验退回的包裹。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'express_number': express_number}.items() if v is not None}
        return self.client.request("/api_tob/inspectSignReceipt/v1.0", params_dict)

    def bind_certificate_buckle(self, erpSkuId: Optional[str] = None, antiFakeCode: Optional[str] = None, certificateNo: Optional[str] = None) -> Dict[str, Any]:
        """
        买家支付成功 30 分钟后可以进行防伪扣的绑定与换绑操作。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'erpSkuId': erpSkuId, 'antiFakeCode': antiFakeCode, 'certificateNo': certificateNo}.items() if v is not None}
        return self.client.request("/api_tob/bindCertificateBuckle/v1.0", params_dict)
