"""
MerchantOnboarding API
"""

from typing import Any, Dict, Optional, List


class MerchantOnboardingApi:
    """MerchantOnboarding API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    def send_sms(self, mobile: str) -> Dict[str, Any]:
        """
        发送短信验证码至商家要入驻 95 分账号对应的手机号。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'mobile': mobile}.items() if v is not None}
        return self.client.request("/api_tob/erpSendSmsCaptcha/v1.0", params_dict)

    def check_sms(self, mobile: str, captcha: str) -> Dict[str, Any]:
        """
        校验验证码是否正确,完成入驻商家基本数据初始化。
        
        Returns:
            响应数据
        """
        params_dict = {k: v for k, v in {'mobile': mobile, 'captcha': captcha}.items() if v is not None}
        return self.client.request("/api_tob/erpCheckSmsCaptcha/v1.0", params_dict)
