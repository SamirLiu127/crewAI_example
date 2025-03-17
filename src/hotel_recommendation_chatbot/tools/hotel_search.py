from crewai.tools import BaseTool
from typing import Dict, List, Any, Union
from .hotel_api import HotelAPI

api = HotelAPI()


class GetHotelDetail(BaseTool):
    name: str = "Get Hotel Detail Tool"
    description: str = "用於取得旅館詳細資料"

    def _run(self, hotel_name: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/details"
        params = {"hotel_name": hotel_name}
        return api.make_request(endpoint, params)

class GuessHotel(BaseTool):
    name: str = "Guess Hotel Tool"
    description: str = "用於取得旅館名稱模糊匹配"

    def _run(self, hotel_name: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/fuzzy_match"
        params = {"hotel_name": hotel_name}
        return api.make_request(endpoint, params)

class GetHotelsByHotelGroupTypes(BaseTool):
    name: str = "Get Hotels By Hotel Group Types Tool"
    description: str = "用於取得縣市列表"

    def _run(self, hotel_group_types: str = 'basic') -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotels"
        params = {"hotel_group_types": hotel_group_types}
        return api.make_request(endpoint, params)

class GetHotelBySupplyName(BaseTool):
    name: str = "Get Hotel By Supply Name Tool"
    description: str = "用於以關鍵字搜尋有包含某項房間備品的旅館"

    def _run(self, supply_name: str) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/supply"
        params = {"supply_name": supply_name}
        return api.make_request(endpoint, params)

class GetHotelByPlan(BaseTool):
    name: str = "Get Hotel By Plan Tool"
    description: str = "用於取得旅館詳細資料"

    def _run(self, hotel_keyword: str, plan_keyword: str, check_in_start_at: str, check_in_end_at: str) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/plans"
        params = {
            "hotel_keyword": hotel_keyword,
            "plan_keyword": plan_keyword,
            "check_in_start_at": check_in_start_at,
            "check_in_end_at": check_in_end_at
        }
        return api.make_request(endpoint, params)
    
class GetHotelRoomByVacancies(BaseTool):
    name: str = "Get Hotel Room By Vacancies Tool"
    description: str = "多條件搜尋可訂旅館"
    original_params: Dict[str, Any] = {
        "hotel_group_types": None,  # 旅館類別
        "check_in": None,           # 入住日期 (ex. 2025-01-01)
        "check_out": None,          # 退房日期 (ex. 2025-01-03)
        "adults": None,             # 成人數
        "children": None,           # 兒童數
        "lowest_price": None,       # 最低價格
        "highest_price": None,      # 最高價格
        "county_ids": [],           # 城市 ID 列表
        "district_ids": [],         # 鄉鎮區 ID 列表
        "hotel_facility_ids": [],   # 旅館設施 ID 列表
        "room_types": [],           # 房型 ID 列表
        "room_facility_ids": [],    # 房間設施 ID 列表
        "has_breakfast": None,      # 是否有早餐
        "has_lunch": None,          # 是否有午餐
        "has_dinner": None          # 是否有晚餐
    }
    
    def _run(self, params: Dict[str, Any]) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/vacancies"
        # 更新參數
        for key, value in self.original_params.items():
            if key in params and params[key] is not None:
                self.original_params[key] = params[key]
        
        return api.make_request(endpoint, self.original_params)
    