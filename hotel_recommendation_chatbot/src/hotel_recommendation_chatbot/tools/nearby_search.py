from crewai.tools import BaseTool
from typing import Dict, List, Any, Union
from .hotel_api import HotelAPI

api = HotelAPI()


class GetNearbyPlaces(BaseTool):
    name: str = "Get Nearby Places Tool"
    description: str = "用於搜索附近地點的工具"
    original_params: Dict[str, Any] = {
        "text_query": None,
        "output_max_num": 10,
        "output_language": "zh-TW",
        "output_place_region": "TW"
    }
    
    def _run(self, params: Dict[str, Any]) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """取得周邊地標"""
        endpoint = "/api/v3/tools/external/gcp/places/nearby_search_with_query"
        for key, value in self.original_params.items():
            if key in params and params[key] is not None:
                self.original_params[key] = params[key]
                
        return api.make_request(endpoint, self.original_params)