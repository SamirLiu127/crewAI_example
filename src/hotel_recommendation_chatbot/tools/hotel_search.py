from crewai.tools import BaseTool
from typing import Dict, List, Any, Union
from .hotel_api import HotelAPI

api = HotelAPI()


class GetHotelDetail(BaseTool):
    name: str = "Get Hotel Detail Tool"
    description: str = """用於取得旅館詳細資料
        - hotel_name (str, required): 旅館名稱
    """

    def _run(self, hotel_name: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/details"
        params = {"hotel_name": hotel_name}
        return api.make_request(endpoint, params)

class GuessHotel(BaseTool):
    name: str = "Guess Hotel Tool"
    description: str = """用於取得旅館名稱模糊匹配
        - hotel_name (str, required): 旅館名稱
    """

    def _run(self, hotel_name: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/fuzzy_match"
        params = {"hotel_name": hotel_name}
        return api.make_request(endpoint, params)

class GetHotelsByHotelGroupTypes(BaseTool):
    name: str = "Get Hotels By Hotel Group Types Tool"
    description: str = """用於取得縣市列表
        - hotel_group_types (str, optional). Defaults to 'basic'.
    """

    def _run(self, hotel_group_types: str = 'basic') -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotels"
        params = {"hotel_group_types": hotel_group_types}
        return api.make_request(endpoint, params)

class GetHotelBySupplyName(BaseTool):
    name: str = "Get Hotel By Supply Name Tool"
    description: str = """用於以關鍵字搜尋有包含某項房間備品的旅館
        - supply_name (str, required): 房間備品名稱
    """

    def _run(self, supply_name: str) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/supply"
        params = {"supply_name": supply_name}
        return api.make_request(endpoint, params)

class GetHotelByPlan(BaseTool):
    name: str = "Get Hotel By Plan Tool"
    description: str = """用於取得旅館詳細資料
        - hotel_keyword (str, optional): 旅館名稱/關鍵字
        - plan_keyword (str, optional): 旅館訂購方案名稱/關鍵字
        - check_in_start_at (str, required): 退房日期 (ex. 2025-01-01)
        - check_in_end_at (str, optional): 退房日期 (ex. 2025-01-03)
    """

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
    description: str = """用於多條件搜尋可訂旅館
        - hotel_group_types (str, optional): 旅館類別, 預設為 'basic'
        - check_in (str, optional): 退房日期 (ex. 2025-01-01)
        - check_out (str, optional): 退房日期 (ex. 2025-01-03)
        - adults (int, optional): 成人數
        - children (int, optional): 兒童數
        - lowest_price (int, optional): 最低價格
        - highest_price (int, optional): 最高價格
        - county_ids[] (list, optional): 城市 ID 列表
        - district_ids[] (list, optional): 鄉鎮區 ID 列表
        - hotel_facility_ids[] (list, optional): 旅館設施 ID 列表
        - room_types[] (list, optional): 房型 ID 列表
        - room_facility_ids[] (list, optional): 房間設施 ID 列表
        - has_breakfast (bool, optional): 是否有早餐
        - has_lunch (bool, optional): 是否有午餐
        - has_dinner (bool, optional): 是否有晚餐
    """
    
    def _run(self, **kwargs) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/vacancies"
        params = {
            "hotel_group_types": kwargs.get("hotel_group_types", "basic"),
        }
        for key, value in kwargs.items():
            params[key] = value
        
        return api.make_request(endpoint, params)
    