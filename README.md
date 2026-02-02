# 95分开放平台 Python SDK

[![PyPI version](https://img.shields.io/badge/pypi-1.0.0-blue)](https://pypi.org/project/jiuwufen-sdk/)
[![Python Version](https://img.shields.io/badge/python-%3E%3D3.7-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

95分开放平台的官方 Python SDK，提供完整的 API 调用能力，包括商品管理、订单处理、库存同步等功能。

## ✨ 特性

- 🐍 **Pythonic 设计** - 符合 Python 编程习惯
- 🔐 **自动签名** - 内置 MD5 + Base64 签名算法
- 🔒 **地址解密** - 支持 AES-ECB 买家地址解密
- 📦 **完整 API** - 覆盖所有开放平台接口
- 🎯 **类型提示** - 完整的类型注解支持
- 🔄 **上下文管理** - 支持 with 语句自动管理资源
- 📝 **详细日志** - 支持调试模式查看请求详情
- ⚡ **高性能** - 基于 requests 的高性能 HTTP 客户端

## 📦 安装

### 使用 pip

```bash
pip install jiuwufen-sdk
```

### 从源码安装

```bash
git clone https://github.com/jiuwufen/python-sdk.git
cd python-sdk
pip install -e .
```

## 🚀 快速开始

### 1. 创建客户端

```python
from jiuwufen_sdk import JiuWuFenClient

client = JiuWuFenClient(
    erp_name="your-erp-name",              # ERP 名称（由95分提供）
    third_party_id="your-third-party-id",   # 第三方应用标识
    merchant_secret="your-merchant-secret", # 商家密钥
    platform_secret="your-platform-secret", # 平台密钥
    base_url="http://d1.95fenapp.com",     # 开发环境
    timeout=30,                             # 请求超时（秒）
    debug=True                              # 开启调试模式
)
```

### 2. 使用上下文管理器

```python
from jiuwufen_sdk import JiuWuFenClient

with JiuWuFenClient(
    erp_name="your-erp-name",
    third_party_id="your-third-party-id",
    merchant_secret="your-merchant-secret",
    platform_secret="your-platform-secret"
) as client:
    response = client.merchant.send_sms_captcha(mobile="13800000000")
    print(response)
```

### 3. 商户入驻

```python
# 发送短信验证码
response = client.merchant.send_sms_captcha(mobile="13800000000")
print(f"验证码已发送: {response}")

# 校验短信验证码
response = client.merchant.check_sms_captcha(
    mobile="13800000000",
    captcha="123456"
)
print(f"应用标识: {response['hearder_name']}")
print(f"应用密钥: {response['secret_key']}")
```

### 4. 商品管理

```python
# 新增商品
response = client.goods.add_order_goods(
    goods_sn="GOODS-2024-001",
    title="Nike Air Max 90 经典复古跑鞋",
    brand_id=2,
    l1_category_id=1,
    l2_category_id=10,
    first_img="https://example.com/nike-air-max-90-main.jpg",
    general_imgs=[
        "https://example.com/nike-air-max-90-1.jpg",
        "https://example.com/nike-air-max-90-2.jpg"
    ],
    price=29900,  # 价格单位：分
    quality=20
)
print("商品添加成功!")
```

### 5. 库存同步

```python
# 库存同步
response = client.inventory.sync_inventory(
    detail=[
        {
            "merchant_sku_code": "SKU-001",
            "sku_id": 1390873,
            "qty": 100,
            "salable_qty": 90
        }
    ]
)
print(f"库存同步结果: {response['sync_result']}")
```

### 6. 订单查询

```python
# 查询订单
response = client.order.get_consign_order_info(
    order_number=["95025032898155673463"],
    page=1,
    page_size=20
)

for order in response.get('order_list', []):
    print(f"订单号: {order['sell_order_number']}")
    print(f"状态: {order['status_desc']}")
```

## 📚 API 列表

### 平台商户入驻 (2个接口)

| 方法 | 说明 |
|------|------|
| `merchant.send_sms_captcha()` | 发送短信验证码 |
| `merchant.check_sms_captcha()` | 校验短信验证码 |

### 商品管理 (11个接口)

| 方法 | 说明 |
|------|------|
| `goods.get_merchant_sku_list()` | 查询SKU列表（绑定关系） |
| `goods.add_order_goods()` | 新增商品 |
| `goods.get_goods_info()` | 查询商品状态信息 |
| `goods.update_price()` | 改价 |
| `goods.cancel_order()` | 下架商品 |
| `goods.update_seller_bargain()` | 卖家议价 |
| `goods.bargain_success()` | 卖家接受还价 |
| `goods.query_properties()` | 获取类目属性 |
| `goods.get_brand_identify_ability()` | 可鉴品牌查询 |
| `goods.copy_on_sale()` | 复制订单上架 |
| `goods.get_reference_price()` | 订单参考价查询 |

### 库存管理 (3个接口)

| 方法 | 说明 |
|------|------|
| `inventory.sync_inventory()` | 库存同步 |
| `inventory.get_inventory_list()` | 库存查询 |
| `inventory.update_stock()` | 同步库存（上下架） |

### 订单管理 (4个接口)

| 方法 | 说明 |
|------|------|
| `order.get_consign_order_info()` | 查询商品订单信息 |
| `order.get_buyer_address()` | 买家地址查询 |
| `order.get_consign_batch_order_list()` | 自送货订单明细查询 |
| `order.get_order_list()` | 获取订单列表（挂售） |

### 物流管理 (1个接口)

| 方法 | 说明 |
|------|------|
| `delivery.delivery_biz()` | 发货 & 重打面单 |

## ⚙️ 配置选项

### 环境配置

```python
# 开发环境
base_url="http://d1.95fenapp.com"

# 测试环境
base_url="http://t1.95fenapp.com"

# 预发环境
base_url="http://stg-www.95fenapp.com"

# 生产环境
base_url="http://www.95fenapp.com"
```

### 超时配置

```python
client = JiuWuFenClient(
    # ... 其他配置
    timeout=30  # 请求超时：30秒
)
```

### 调试模式

```python
client = JiuWuFenClient(
    # ... 其他配置
    debug=True  # 开启调试模式，打印请求和响应详情
)
```

## 🔧 高级功能

### 错误处理

```python
from jiuwufen_sdk import JiuWuFenClient, ApiException

try:
    response = client.goods.add_order_goods(**params)
    print(f"成功: {response}")
except ApiException as e:
    print(f"错误码: {e.code}")
    print(f"错误信息: {e.message}")
    print(f"请求ID: {e.req_id}")
    
    if e.is_business_error():
        # 处理业务错误
        print("业务错误，请检查参数")
    elif e.is_network_error():
        # 处理网络错误
        print("网络错误，请稍后重试")
```

### 地址解密

```python
from jiuwufen_sdk.utils.signature import SignatureUtil

# 获取加密的买家地址
response = client.order.get_buyer_address(order_number="95025032898155673463")

# 解密地址
key = b"your-platform-secret"
decrypted_address = SignatureUtil.decrypt_address(
    response['address'], 
    key
)
print(f"买家地址: {decrypted_address}")
```

### 签名验证（用于回调）

```python
from jiuwufen_sdk.utils.signature import SignatureUtil

# 初始化签名工具
util = SignatureUtil(merchant_secret, platform_secret)

# 验证回调签名
params = {
    "goods_sn": "GOODS-001",
    "price": 29900,
    # ... 其他参数
}

received_token = "received_token_from_callback"

if util.verify_signature(params, received_token):
    print("签名验证通过")
else:
    print("签名验证失败")
```

## 🧪 测试

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 运行测试并生成覆盖率报告
pytest --cov=jiuwufen_sdk --cov-report=html

# 查看覆盖率报告
open htmlcov/index.html
```

## 📖 文档

- [API 详细文档](docs/API.md)
- [快速开始指南](docs/QUICKSTART.md)
- [常见问题](docs/FAQ.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 📞 技术支持

- GitHub: https://github.com/jiuwufen/python-sdk
- Issues: https://github.com/jiuwufen/python-sdk/issues
- Email: support@95fenapp.com

## 🎯 版本历史

### v1.0.0 (2024-02-02)

- ✅ 完整的 API 实现（21个接口）
- ✅ Pythonic 设计风格
- ✅ 自动签名和加解密
- ✅ 完善的错误处理
- ✅ 详细的文档和示例
- ✅ 完整的单元测试
