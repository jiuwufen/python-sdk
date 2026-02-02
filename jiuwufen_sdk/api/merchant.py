"""
Merchant API
"""

from typing import Any, Dict, Optional, List


class MerchantApi:
    """Merchant API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client

    
    def send_sms_captcha(self, mobile: str) -> Dict[str, Any]:
        """
        发送短信验证码
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/erpSendSmsCaptcha/v1.0", {'mobile': mobile})

    
    def check_sms_captcha(self, mobile: str, captcha: str) -> Dict[str, Any]:
        """
        校验短信验证码
        
        Returns:
            响应数据
        """
        return self.client.request("/api_tob/erpCheckSmsCaptcha/v1.0", {'mobile': mobile, 'captcha': captcha})
