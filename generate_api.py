#!/usr/bin/env python3
"""
Python SDK API 和模型生成器
"""

import os
from pathlib import Path

BASE_DIR = Path("/Users/admin/promptflow-open/sdk/python-sdk/jiuwufen_sdk")

# API 定义
APIS = {
    "merchant": {
        "class_name": "MerchantApi",
        "methods": [
            {
                "name": "send_sms_captcha",
                "path": "/api_tob/erpSendSmsCaptcha/v1.0",
                "doc": "发送短信验证码",
                "params": ["mobile: str"],
            },
            {
                "name": "check_sms_captcha",
                "path": "/api_tob/erpCheckSmsCaptcha/v1.0",
                "doc": "校验短信验证码",
                "params": ["mobile: str", "captcha: str"],
            },
        ],
    },
    "goods": {
        "class_name": "GoodsApi",
        "methods": [
            {
                "name": "get_merchant_sku_list",
                "path": "/api_tob/merchantSkuList/v1.0",
                "doc": "查询SKU列表（绑定关系）",
                "params": ["**kwargs"],
            },
            {
                "name": "add_order_goods",
                "path": "/api_tob/addOrderGoods/v1.0",
                "doc": "新增商品",
                "params": ["**kwargs"],
            },
            {
                "name": "get_goods_info",
                "path": "/api_tob/goodsInfo/v1.0",
                "doc": "查询商品状态信息",
                "params": ["goods_sn: str"],
            },
            {
                "name": "update_price",
                "path": "/api_tob/updatePrice/v1.0",
                "doc": "改价",
                "params": ["goods_sn: str", "price: int"],
            },
            {
                "name": "cancel_order",
                "path": "/api_tob/cancelOrder/v1.0",
                "doc": "下架商品",
                "params": ["goods_sn: str"],
            },
            {
                "name": "update_seller_bargain",
                "path": "/api_tob/updateSellerBargain/v1.0",
                "doc": "卖家议价",
                "params": ["goods_sn: str", "price: int"],
            },
            {
                "name": "bargain_success",
                "path": "/api_tob/bargainSuccess/v1.0",
                "doc": "卖家接受还价",
                "params": ["goods_sn: str"],
            },
            {
                "name": "query_properties",
                "path": "/api_tob/query_properties/v1.0",
                "doc": "获取类目属性",
                "params": ["child_category_id: int"],
            },
            {
                "name": "get_brand_identify_ability",
                "path": "/api_tob/get_brand_identify_ability/v1.0",
                "doc": "可鉴品牌查询",
                "params": ["l1_category_id: int", "brand_name: str"],
            },
            {
                "name": "copy_on_sale",
                "path": "/api_tob/copyOnSale/v1.0",
                "doc": "复制订单上架",
                "params": ["goods_sn: str"],
            },
            {
                "name": "get_reference_price",
                "path": "/api_tob/referencePrice/v1.0",
                "doc": "订单参考价查询",
                "params": ["goods_sn: str"],
            },
        ],
    },
    "inventory": {
        "class_name": "InventoryApi",
        "methods": [
            {
                "name": "sync_inventory",
                "path": "/api_tob/inventory/sync/v1.0",
                "doc": "库存同步",
                "params": ["detail: list"],
            },
            {
                "name": "get_inventory_list",
                "path": "/api_tob/inventory/list/v1.0",
                "doc": "库存查询",
                "params": ["detail: list"],
            },
            {
                "name": "update_stock",
                "path": "/api_tob/updateStock/v1.0",
                "doc": "同步库存（上下架）",
                "params": ["goods_sn: str", "stock: int"],
            },
        ],
    },
    "order": {
        "class_name": "OrderApi",
        "methods": [
            {
                "name": "get_consign_order_info",
                "path": "/api_tob/consignOrderInfo/v1.0",
                "doc": "查询商品订单信息",
                "params": ["**kwargs"],
            },
            {
                "name": "get_buyer_address",
                "path": "/api_tob/order/buyerAddress",
                "doc": "买家地址查询",
                "params": ["order_number: str"],
            },
            {
                "name": "get_consign_batch_order_list",
                "path": "/api_tob/consignBatchOrderList/v1.0",
                "doc": "自送货订单明细查询",
                "params": ["batch_number: str"],
            },
            {
                "name": "get_order_list",
                "path": "/api_tob/getOrderList/v1.0",
                "doc": "获取订单列表（挂售）",
                "params": ["**kwargs"],
            },
        ],
    },
    "delivery": {
        "class_name": "DeliveryApi",
        "methods": [
            {
                "name": "delivery_biz",
                "path": "/api_tob/delivery/bizDelivery/v1.0",
                "doc": "发货 & 重打面单",
                "params": ["**kwargs"],
            },
        ],
    },
}


def generate_api_class(module_name: str, api_def: dict) -> str:
    """生成 API 类代码"""
    class_name = api_def["class_name"]
    methods = api_def["methods"]
    
    code = f'''"""
{class_name.replace("Api", "")} API
"""

from typing import Any, Dict, Optional, List


class {class_name}:
    """{class_name.replace("Api", "")} API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client
'''
    
    for method in methods:
        method_name = method["name"]
        path = method["path"]
        doc = method["doc"]
        params = method["params"]
        
        # 构建参数列表
        param_list = ", ".join(params) if params else ""
        
        # 构建参数字典
        if params == ["**kwargs"]:
            param_dict = "kwargs"
        else:
            param_dict_items = []
            for param in params:
                param_name = param.split(":")[0].strip()
                param_dict_items.append(f"'{param_name}': {param_name}")
            param_dict = "{" + ", ".join(param_dict_items) + "}"
        
        code += f'''
    
    def {method_name}(self, {param_list}) -> Dict[str, Any]:
        """
        {doc}
        
        Returns:
            响应数据
        """
        return self.client.request("{path}", {param_dict})
'''
    
    return code


def main():
    """主函数"""
    print("开始生成 Python SDK API 类...")
    
    api_dir = BASE_DIR / "api"
    api_dir.mkdir(exist_ok=True)
    
    # 生成 __init__.py
    init_imports = []
    init_all = []
    
    for module_name, api_def in APIS.items():
        class_name = api_def["class_name"]
        
        # 生成 API 类文件
        code = generate_api_class(module_name, api_def)
        file_path = api_dir / f"{module_name}.py"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        
        print(f"✅ 生成: api/{module_name}.py")
        
        init_imports.append(f"from .{module_name} import {class_name}")
        init_all.append(class_name)
    
    # 生成 api/__init__.py
    init_code = '"""API 模块"""\n\n'
    init_code += '\n'.join(init_imports)
    init_code += '\n\n__all__ = [\n'
    init_code += ',\n'.join(f'    "{name}"' for name in init_all)
    init_code += '\n]\n'
    
    with open(api_dir / "__init__.py", 'w', encoding='utf-8') as f:
        f.write(init_code)
    
    print(f"✅ 生成: api/__init__.py")
    print(f"\n✨ 所有 API 类生成完成！")


if __name__ == "__main__":
    main()
