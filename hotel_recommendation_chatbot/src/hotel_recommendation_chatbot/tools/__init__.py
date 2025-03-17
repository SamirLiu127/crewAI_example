# 工具模塊初始化文件 

from .hotel_parameters import *
from .hotel_search import *
from .nearby_search import *

__all__ = [
    "GetCounties", "GetDistricts", "GetHotelGroupTypes", "GetHotelFacilities", "GetRoomTypeFacilities", "GetRoomTypeBedTypes",  # hotel_parameters 
    "GetHotelDetail", "GuessHotel", "GetHotelsByHotelGroupTypes", "GetHotelBySupplyName", "GetHotelByPlan", "GetHotelRoomByVacancies",  # hotel_search
    "GetNearbyPlaces"  # nearby_search
    ]

hotel_parameters_tools = [
    GetCounties(),
    GetDistricts(),
    GetHotelGroupTypes(),
    GetHotelFacilities(),
    GetRoomTypeFacilities(),
    GetRoomTypeBedTypes()
]

hotel_search_tools = [
    GetHotelDetail(),
    GuessHotel(),
    GetHotelsByHotelGroupTypes(),
    GetHotelBySupplyName(),
    GetHotelByPlan(),
    GetHotelRoomByVacancies()
]

nearby_search_tools = [
    GetNearbyPlaces()
]