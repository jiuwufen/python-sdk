"""
MerchantOnboarding API
"""

from typing import Any, Dict


class MerchantOnboardingApi:
    """MerchantOnboarding API"""

    def __init__(self, client):
        self.client = client

    def send_sms(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        发送短信验证码至商家要入驻 95 分账号对应的手机号。

        请求体字段（树状层级，与文档点分路径一致）:
    - mobile (string, 必填): 商家 95 分账号对应手机号

        响应 data 内常见字段（树状层级，供对照文档）:
    - data (object, 必填): 返回数据
    - req_id (string, 必填): 请求 ID
    - status (int, 必填): 状态码(0 成功)

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/erpSendSmsCaptcha/v1.0", body)

    def check_sms(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        校验验证码是否正确,完成入驻商家基本数据初始化。

        请求体字段（树状层级，与文档点分路径一致）:
    - captcha (string, 必填): 验证码
    - mobile (string, 必填): 手机号

        响应 data 内常见字段（树状层级，供对照文档）:
      - data.hearder_name (string, 必填): 平台商户应用标识
      - data.secret_key (string, 必填): 平台商户应用密钥
    - status (int, 必填): 状态码

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("/api_tob/erpCheckSmsCaptcha/v1.0", body)
