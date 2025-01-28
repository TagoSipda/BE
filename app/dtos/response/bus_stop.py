from typing import List, Optional
from pydantic import BaseModel


# Pydantic DTO 정의
class GetBusStopResponseDTO(BaseModel):
    id: Optional[int]
    name: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    arrivals: Optional[List[dict]]
    stop_bus_routes: Optional[List[dict]]


class SearchBusStopsResponseDTO(BaseModel):
    bus_stops: List[GetBusStopResponseDTO]
