"""
95分开放平台 Python SDK

提供完整的 API 调用能力，包括商品管理、订单处理、库存同步等功能。
"""

__version__ = "1.1.0"
__author__ = "95分开放平台团队"
__email__ = "support@95fenapp.com"

from .client import JiuWuFenClient
from .exceptions import ApiException

__all__ = ["JiuWuFenClient", "ApiException"]
