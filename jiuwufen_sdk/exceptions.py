"""
SDK 异常类
"""


class ApiException(Exception):
    """
    API 异常
    
    Attributes:
        code: 错误码（-1: 网络错误，0: 成功，>0: 业务错误）
        message: 错误信息
        req_id: 请求 ID
    """
    
    def __init__(self, code: int, message: str, req_id: str = ""):
        """
        初始化异常
        
        Args:
            code: 错误码
            message: 错误信息
            req_id: 请求 ID
        """
        self.code = code
        self.message = message
        self.req_id = req_id
        super().__init__(self._format_message())
    
    def _format_message(self) -> str:
        """格式化错误信息"""
        if self.req_id:
            return f"[{self.code}] {self.message} (req_id: {self.req_id})"
        return f"[{self.code}] {self.message}"
    
    def is_business_error(self) -> bool:
        """是否为业务错误"""
        return self.code > 0
    
    def is_network_error(self) -> bool:
        """是否为网络错误"""
        return self.code == -1
    
    def __str__(self) -> str:
        return self._format_message()
    
    def __repr__(self) -> str:
        return f"ApiException(code={self.code}, message='{self.message}', req_id='{self.req_id}')"
