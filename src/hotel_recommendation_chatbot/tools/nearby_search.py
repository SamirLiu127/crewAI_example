from crewai.tools import BaseTool
from typing import Dict, List, Any, Union
from .hotel_api import HotelAPI

api = HotelAPI()


class GetNearbyPlaces(BaseTool):
    name: str = "Get Nearby Places Tool"
    description: str = "用於搜索附近地點的工具"
    
    def _run(self, text_query: str, output_max_num: int = 10, output_language: str = "zh-TW", output_place_region: str = "TW") -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """取得周邊地標"""
        endpoint = "/api/v3/tools/external/gcp/places/nearby_search_with_query"
        params = {
            "text_query": text_query,
            "output_max_num": output_max_num,
            "output_language": output_language,
            "output_place_region": output_place_region
        }
        return api.make_request(endpoint, params)