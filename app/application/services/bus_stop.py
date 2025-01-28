from abc import ABC, abstractmethod

from app.application.use_cases.bus_stop import BusStopUseCase
from app.dtos.request.bus_stop import GetBusStopRequestDTO
from app.dtos.request.bus_stop import SearchBusStopsRequestDTO
from app.dtos.response.bus_stop import GetBusStopResponseDTO
from app.dtos.response.bus_stop import SearchBusStopsResponseDTO


class BusStopService(BusStopUseCase):
    def find_by_id(self, dto: GetBusStopRequestDTO) -> GetBusStopResponseDTO:
        return GetBusStopResponseDTO(
            id=dto.id, name="temp", lat=10, lng=10, arrivals=[], stop_bus_routes=[]
        )

    def search_bus_stops(
        self, dto: SearchBusStopsRequestDTO
    ) -> SearchBusStopsResponseDTO:
        bus_stops = [
            GetBusStopResponseDTO(
                id=1, name="temp", lat=10, lng=10, arrivals=[], stop_bus_routes=[]
            ),
            GetBusStopResponseDTO(
                id=2, name="temp2", lat=20, lng=10, arrivals=[], stop_bus_routes=[]
            ),
        ]

        return SearchBusStopsResponseDTO(bus_stops=bus_stops)
