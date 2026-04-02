"""
DigitalProduct API
"""

from typing import Any, Dict


class DigitalProductApi:
    """DigitalProduct API"""

    def __init__(self, client):
        self.client = client

    def examining_config(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        查询 3C 数码产品的质检项配置。

        请求体字段（树状层级，与文档点分路径一致）:
    - template_id (long, 必填): 模版 ID

        响应 data 内常见字段（树状层级，供对照文档）:
      - data.first_examining_list ([]object, 必填): 一级质检项列表
        - data.first_examining_list.key (string, 必填): 一级质检项 Key
        - data.first_examining_list.second_examining_list ([]object, 必填): 二级质检项列表
          - data.first_examining_list.second_examining_list.key (string, 必填): 二级质检项 Key
          - data.first_examining_list.second_examining_list.options ([]string, 必填): 二级质检项选择列表
          - data.first_examining_list.second_examining_list.third_examining_list ([]object, 必填): 三级质检项列表
            - data.first_examining_list.second_examining_list.third_examining_list.key (string, 必填): 三级质检项 Key
            - data.first_examining_list.second_examining_list.third_examining_list.second_examining_category_id (int, 必填): 二级类目 ID
            - data.first_examining_list.second_examining_list.third_examining_list.sub_examining_list (object, 必填): 三级质检项选项列表
              - data.first_examining_list.second_examining_list.third_examining_list.sub_examining_list.checkbox ([]string, 必填): 多选选项
              - data.first_examining_list.second_examining_list.third_examining_list.sub_examining_list.radio ([]string, 必填): 单选选项
            - data.first_examining_list.second_examining_list.third_examining_list.title (string, 必填): 三级质检项名称
            - data.first_examining_list.second_examining_list.third_examining_list.type (string, 必填): 控件类型 (checkbox, radio)
          - data.first_examining_list.second_examining_list.title (string, 必填): 二级质检项名称
          - data.first_examining_list.second_examining_list.type (string, 必填): 控件类型 (input, checkbox, radio, textarea, upload_img)
        - data.first_examining_list.title (string, 必填): 一级质检项名称

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/examiningConfig/v1.0", body)

    def imei_query(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        查询设备 IMEI 上架状态。

        请求体字段（树状层级，与文档点分路径一致）:
    - imei (string, 必填): 设备唯一标识

        响应 data 内常见字段（树状层级，供对照文档）:
      - data.status (int, 必填): 状态 (1: 已上架, 2: 未上架)

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/imei/v1.0", body)

    def digital_super_sale(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        平台商家一键出售 3C 数码商品。

        请求体字段（树状层级，与文档点分路径一致）:
    - address (object, 必填): 卖家地址
      - address.city (string, 必填): 市
      - address.county (string, 必填): 区
      - address.mobile (string, 必填): 联系方式
      - address.name (string, 必填): 姓名
      - address.province (string, 必填): 省
      - address.street (string, 必填): 详细地址
    - examining_list ([]object, 必填): 质检项列表
      - examining_list.key (string, 必填): 一级质检项 Key
      - examining_list.second_examining_list ([]object, 必填): 二级质检项列表
        - examining_list.second_examining_list.key (string, 必填): 二级质检项 Key
        - examining_list.second_examining_list.third_examining_list ([]object, 选填): 三级质检项列表
          - examining_list.second_examining_list.third_examining_list.imgs ([]string, 选填): 质检图片
          - examining_list.second_examining_list.third_examining_list.key (string, 必填): 三级质检项 Key
          - examining_list.second_examining_list.third_examining_list.status (bool, 必填): 质检状态 (true: 正常, false: 异常)
          - examining_list.second_examining_list.third_examining_list.value (string, 必填): 三级质检项 Value
        - examining_list.second_examining_list.value (string, 必填): 二级质检项 Value
    - flaw_imgs ([]string, 选填): 瑕疵图 (1-15张)
    - general_imgs ([]string, 必填): 实拍图 (5-15张)
    - goods_sn (string, 必填): 商品唯一标识 (5-128字符)
    - imei (string, 必填): 设备唯一标识
    - internal_enterprise_id (string, 选填): 商家内部企业 ID
    - price (int, 必填): 售价 (分)
    - product_source_type (int, 选填): 货品来源 (1: B端特供)
    - quality (int, 必填): 成色
    - result_desc (string, 必填): 检测结果描述
    - sku_id (long, 必填): 95 SkuId
    - template_id (int, 必填): 模版 ID

        响应 data 内常见字段（树状层级，供对照文档）:
      - data.result (bool, 必填): 操作结果

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/digitalSuperSale/v1.0", body)

    def digital_super_sale_v2(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        自研商家一键出售 3C 数码商品 (V2 版本)。

        请求体字段（树状层级，与文档点分路径一致）:
    - address (object, 必填): 卖家地址
      - address.city (string, 必填): 市
      - address.county (string, 必填): 区
      - address.mobile (string, 必填): 联系方式
      - address.name (string, 必填): 姓名
      - address.province (string, 必填): 省
      - address.street (string, 必填): 详细地址
    - examining_list ([]object, 必填): 质检项列表
      - examining_list.imgs ([]string, 选填): 质检项异常图片数组
      - examining_list.key (string, 必填): 质检项 Key
    - flaw_imgs ([]string, 选填): 瑕疵图 (1-15张)
    - general_imgs ([]string, 必填): 实拍图 (5-15张)
    - goods_sn (string, 必填): 商品唯一标识 (5-128字符)
    - imei (string, 必填): 设备唯一标识
    - price (int, 必填): 售价 (分)
    - quality (string, 必填): 成色名称 (如: 准新机)
    - result_desc (string, 必填): 检测结果描述
    - sku_id (long, 必填): 三方 SkuId

        响应 data 内常见字段（树状层级，供对照文档）:
      - data.result (bool, 必填): 操作结果

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/digitalSuperSale/v2.0", body)

    def inspect_sign_receipt(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        商家确认签收后验退回的包裹。

        请求体字段（树状层级，与文档点分路径一致）:
    - express_number (string, 必填): 后验退回快递单号

        响应 data 内常见字段（树状层级，供对照文档）:
      - data.status (int, 必填): 状态 (1: 成功, 2: 失败)

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/inspectSignReceipt/v1.0", body)

    def bind_certificate_buckle(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        买家支付成功 30 分钟后可以进行防伪扣的绑定与换绑操作。

        请求体字段（树状层级，与文档点分路径一致）:
    - antiFakeCode (string, 选填): 防伪扣
    - certificateNo (string, 选填): 证书编号
    - erpSkuId (string, 选填): goods_sn

        响应 data 内常见字段（树状层级，供对照文档）:
      - data.data (bool, 必填): 是否成功

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/bindCertificateBuckle/v1.0", body)
