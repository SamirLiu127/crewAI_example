import requests
from typing import Dict, List, Optional, Union, Any
import os


class HotelAPI:
    def __init__(self):
        # 使用環境變數替代匯入設定
        self.base_url = os.environ.get("RACCOONAI_BASE_URL", "https://api.example.com")
        self.headers = {
            "Authorization": os.environ.get("RACCOONAI_API_KEY", ""),
            "accept": "application/json"
        }
    
    def make_request(self, endpoint: str, params: Optional[Dict] = None) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """通用 API 請求方法，返回類型可能是字典或字典列表"""
        try:
            response = requests.get(
                url=f"{self.base_url}{endpoint}",
                headers=self.headers,
                params=params,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API 請求錯誤: {str(e)}")
            return {"error": str(e)}