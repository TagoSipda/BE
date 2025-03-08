from abc import ABC, abstractmethod
from fastapi import Depends

from app.application.use_cases.bus_stop import BusStopUseCase
from app.application.repositories.bus_stop import BusStopRepository
from app.application.repositories.bus_route import BusRouteRepository
from app.application.use_cases.bus_stop import GetBusStopRequestDTO
from app.application.use_cases.bus_stop import SearchBusStopsRequestDTO
from app.application.use_cases.bus_stop import GetBusStopResponseDTO
from app.application.use_cases.bus_stop import SearchBusStopsResponseDTO
from app.domain.entities.bus_stop import BusStopEntityProjection


class BusStopUseCaseImpl(BusStopUseCase):
    def __init__(
        self,
        bus_stop_repository: BusStopRepository,
        bus_route_repository: BusRouteRepository,
    ):
        self.bus_stop_repository = bus_stop_repository
        self.bus_route_repository = bus_route_repository

    def get_bus_stop(self, dto: GetBusStopRequestDTO) -> GetBusStopResponseDTO:
        bus_stop: BusStopEntityProjection = self.bus_stop_repository.find_by_id(
            dto.id, dto.requested_field
        )
        stop_bus_routes = []

        # if "stop_bus_routes" in dto.requested_field:
        #     stop_bus_routes = self.bus_route_repository.find_by_id_list(
        #         bus_stop.stop_bus_route_ids
        #     )
        # else:
        #     stop_bus_routes = None

        # DTO 변환 로직을 유스케이스 내부로 이동
        return GetBusStopResponseDTO(
            stop_bus_routes=stop_bus_routes, **bus_stop.__dict__
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
