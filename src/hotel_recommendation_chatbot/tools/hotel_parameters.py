from crewai.tools import BaseTool
from typing import Dict, List, Any, Union
from .hotel_api import HotelAPI
from pydantic import BaseModel, ConfigDict

api = HotelAPI()


class GetCounties(BaseTool):
    name: str = "Get Counties Tool"
    description: str = "取得台灣旅館縣市列表"

    def _run(self, page: int = 1) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/counties"
        params = {"page": page}
        return api.make_request(endpoint, params)


class GetDistricts(BaseTool):
    name: str = "Get Districts Tool"
    description: str = "取得台灣旅館鄉鎮區列表"

    def _run(self, page: int = 1) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/districts"
        params = {"page": page}
        return api.make_request(endpoint, params)


class GetHotelGroupTypes(BaseTool):
    name: str = "Get Hotel Group Types Tool"
    description: str = "取得台灣旅館集團類型列表"

    def _run(self, page: int = 1) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel_group/types"
        params = {"page": page}
        return api.make_request(endpoint, params)


class GetHotelFacilities(BaseTool):
    name: str = "Get Hotel Facilities Tool"
    description: str = "取得台灣旅館設施列表"

    def _run(self, page: int = 1) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/facilities"
        params = {"page": page}
        return api.make_request(endpoint, params)


class GetRoomTypeFacilities(BaseTool):
    name: str = "Get Room Type Facilities Tool"
    description: str = "取得台灣旅館房間設施列表"

    def _run(self, page: int = 1) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/room_type/facilities"
        params = {"page": page}
        return api.make_request(endpoint, params)


class GetRoomTypeBedTypes(BaseTool):
    name: str = "Get Room Type Bed Types Tool"
    description: str = "取得台灣旅館房間床型列表"

    def _run(self, page: int = 1) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        endpoint = "/api/v3/tools/interview_test/taiwan_hotels/hotel/room_type/bed_types"
        params = {"page": page}
        return api.make_request(endpoint, params)


class HotelParameters(BaseModel):
    # fields...
    
    model_config = ConfigDict(
        # same config options as before
    )
