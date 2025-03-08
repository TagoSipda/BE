from abc import ABC, abstractmethod
from typing import List, Optional
from pydantic import BaseModel

from app.application.repositories.bus_stop import BusStopRepository
from app.application.repositories.bus_route import BusRouteRepository


class GetBusStopRequestDTO(BaseModel):
    id: int
    requested_field: List[str]


class SearchBusStopsRequestDTO(BaseModel):
    name: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    top_k: int
    requested_fields: List[str]


class GetBusStopResponseDTO(BaseModel):
    id: Optional[int]
    name: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    arrivals: Optional[List[dict]]
    stop_bus_routes: Optional[List[dict]]


class SearchBusStopsResponseDTO(BaseModel):
    bus_stops: List[GetBusStopResponseDTO]


class BusStopUseCase(ABC):
    @abstractmethod
    def __init__(
        self,
        bus_stop_repository: BusStopRepository,
        bus_route_repository: BusRouteRepository,
    ):
        pass

    @abstractmethod
    def get_bus_stop(self, dto: GetBusStopRequestDTO) -> GetBusStopResponseDTO:
        pass

    @abstractmethod
    def search_bus_stops(
        self, dto: SearchBusStopsRequestDTO
    ) -> SearchBusStopsResponseDTO:
        pass
