"""
基础使用示例
"""

from jiuwufen_sdk import JiuWuFenClient, ApiException


def main():
    """主函数"""
    
    # 创建客户端
    client = JiuWuFenClient(
        erp_name="your-erp-name",
        third_party_id="your-third-party-id",
        merchant_secret="your-merchant-secret",
        platform_secret="your-platform-secret",
        base_url="http://d1.95fenapp.com",
        debug=True
    )
    
    try:
        # 示例1: 发送短信验证码
        print("=== 示例1: 发送短信验证码 ===")
        response = client.merchant.send_sms_captcha(mobile="13800000000")
        print(f"验证码已发送: {response}")
        
        # 示例2: 校验短信验证码
        print("\n=== 示例2: 校验短信验证码 ===")
        response = client.merchant.check_sms_captcha(
            mobile="13800000000",
            captcha="123456"
        )
        print(f"校验成功: {response}")
        
        # 示例3: 新增商品
        print("\n=== 示例3: 新增商品 ===")
        response = client.goods.add_order_goods(
            goods_sn="GOODS-2024-001",
            title="Nike Air Max 90",
            brand_id=2,
            l1_category_id=1,
            l2_category_id=10,
            first_img="https://example.com/img1.jpg",
            general_imgs=["https://example.com/img2.jpg"],
            price=29900,
            quality=20
        )
        print(f"商品添加成功: {response}")
        
        # 示例4: 库存同步
        print("\n=== 示例4: 库存同步 ===")
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
        print(f"库存同步结果: {response}")
        
        # 示例5: 查询订单
        print("\n=== 示例5: 查询订单 ===")
        response = client.order.get_consign_order_info(
            order_number=["95025032898155673463"],
            page=1,
            page_size=20
        )
        print(f"订单列表: {response}")
        
        # 示例6: 错误处理
        print("\n=== 示例6: 错误处理示例 ===")
        try:
            client.goods.get_goods_info(goods_sn="INVALID_GOODS_SN")
        except ApiException as e:
            print(f"业务错误:")
            print(f"  错误码: {e.code}")
            print(f"  错误信息: {e.message}")
            print(f"  请求ID: {e.req_id}")
            
            if e.is_business_error():
                print(f"  类型: 业务错误")
            elif e.is_network_error():
                print(f"  类型: 网络错误")
        
        print("\n=== 基础示例完成 ===")
        
    except ApiException as e:
        print(f"API 异常: {e}")
    except Exception as e:
        print(f"未知异常: {e}")
    finally:
        # 关闭客户端
        client.close()


# 使用上下文管理器的方式
def context_manager_example():
    """上下文管理器示例"""
    with JiuWuFenClient(
        erp_name="your-erp-name",
        third_party_id="your-third-party-id",
        merchant_secret="your-merchant-secret",
        platform_secret="your-platform-secret"
    ) as client:
        response = client.merchant.send_sms_captcha(mobile="13800000000")
        print(response)


if __name__ == "__main__":
    main()
