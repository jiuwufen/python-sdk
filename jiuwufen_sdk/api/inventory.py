"""
Inventory API
"""

from typing import Any, Dict


class InventoryApi:
    """Inventory API"""

    def __init__(self, client):
        self.client = client

    def inventory_sync(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        95 分平台的库存变更,三方要保证 95 分库存售出操作了发货确认后实时同步总库存的变更。

        请求体字段（树状层级，与文档点分路径一致）:
    - detail ([]InventorySyncItem, 必填): 详情 (最大 100)
      - detail.batch_id (string, 选填): 批次号 (美妆类目必填)
      - detail.expire_date (string, 选填): 到期时间 (yyyy-MM-dd HH:mm:ss)
      - detail.is_new (long, 选填): 成色
      - detail.lock_qty (long, 选填): 95 预占库存
      - detail.mapping_type (long, 选填): 绑定关系维护类型 (0: 平台维护, 1: 商家维护, 默认 0)
      - detail.merchant_sku_code (string, 必填): 商家商品编码
      - detail.production_date (string, 选填): 生产时间 (yyyy-MM-dd HH:mm:ss)
      - detail.qty (long, 选填): 实际库存
      - detail.salable_qty (long, 必填): 可售库存 (= 实际库存 - 预占库存)
      - detail.sku_id (long, 必填): 95 SkuId

        响应 data 内常见字段（树状层级，供对照文档）:
      - data.fail_list ([]InventorySyncResult, 必填): 失败列表
        - data.fail_list.code (long, 必填): 结果代码 (4001: 商品编码已删除)
        - data.fail_list.merchant_code (string, 必填): 商家编码
        - data.fail_list.msg (string, 必填): 失败原因
      - data.succ_list ([]InventorySyncResult, 必填): 成功列表
        - data.succ_list.code (long, 必填): 结果代码 (0: 成功)
        - data.succ_list.merchant_code (string, 必填): 商家编码
        - data.succ_list.msg (string, 必填): 说明
      - data.sync_result (bool, 必填): 是否更新成功

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/inventory/sync/v1.0", body)

    def inventory_list(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        查询当前库存状态。

        请求体字段（树状层级，与文档点分路径一致）:
    - detail ([]InventoryListReqItem, 必填): 详情 (最大 100)
      - detail.merchant_sku_code (string, 必填): 商家商品编码
      - detail.sku_id (long, 选填): 95 SkuId

        响应 data 内常见字段（树状层级，供对照文档）:
      - data.detail ([]InventoryListItem, 必填): 库存详情列表
        - data.detail.available_qty (long, 必填): 上架中库存
        - data.detail.external_salable_qty (long, 必填): 三方可售库存
        - data.detail.lock_qty (long, 必填): 预占库存
        - data.detail.merchant_sku_code (string, 必填): 商家商品编码
        - data.detail.sku_id (long, 必填): 95 SkuId

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/inventory/list/v1.0", body)

    def update_stock(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        同步库存 (UpdateStock)

        请求体字段（树状层级，与文档点分路径一致）:
    - goods_sn (string, 必填): 第三方商品的唯一标识
    - stock (int, 必填): 1: 解库存 (上架), 0: 锁库存 (下架)

        响应 data 内常见字段（树状层级，供对照文档）:
    - data (object, 必填): 数据
    - msg (string, 必填): 返回信息
    - status (int, 必填): 状态 (0: 成功, 1: 失败)

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/updateStock/v1.0", body)
