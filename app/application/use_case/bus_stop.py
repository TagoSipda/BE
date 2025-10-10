from typing import List, Optional
from app.application.interfaces.outbound.repository.bus_stop import BusStopRepository
from app.application.interfaces.outbound.repository.bus_route import BusRouteRepository
from app.application.interfaces.inbound.graphql.dto import (
    BusStopOutputDTO,
    BusArrivalInfoOutputDTO,
)
from app.domain.entities.bus_stop import BusStopEntity
from app.domain.entities.bus_arrival import BusArrivalInfoEntity


class BusStopUseCaseImpl:
    """버스 정류장 UseCase 구현체"""

    def __init__(
        self,
        bus_stop_repository: BusStopRepository,
        bus_route_repository: BusRouteRepository,
    ):
        self.bus_stop_repository = bus_stop_repository
        self.bus_route_repository = bus_route_repository

    def _entity_to_dto(self, entity: BusStopEntity) -> BusStopOutputDTO:
        """BusStopEntity를 BusStopOutputDTO로 변환"""
        # arrivals 변환
        arrivals_dto = None
        if hasattr(entity, "arrivals") and entity.arrivals is not None:
            arrivals_dto = [
                BusArrivalInfoOutputDTO(
                    bus_route_id=arrival.bus_route_id,
                    next_bus_stop_name=arrival.next_bus_stop_name,
                    first_estimated_arrival_time=arrival.first_estimated_arrival_time,
                    second_estimated_arrival_time=arrival.second_estimated_arrival_time,
                    first_remaining_stops=arrival.first_remaining_stops,
                    second_remaining_stops=arrival.second_remaining_stops,
                    first_congestion_level=arrival.first_congestion_level,
                    second_congestion_level=arrival.second_congestion_level,
                    first_remaining_seats=arrival.first_remaining_seats,
                    second_remaining_seats=arrival.second_remaining_seats,
                )
                for arrival in entity.arrivals
            ]

        return BusStopOutputDTO(
            id=entity.id,
            name=entity.name,
            lat=entity.lat,
            lng=entity.lng,
            arrivals=arrivals_dto,
            stop_bus_route_ids=(
                entity.stop_bus_route_ids
                if hasattr(entity, "stop_bus_route_ids")
                else None
            ),
        )

    async def get_bus_stop(self, id: int) -> BusStopOutputDTO:
        """버스 정류장 조회"""
        requested_fields = [
            "id",
            "name",
            "lat",
            "lng",
            "arrivals",
            "stop_bus_route_ids",
        ]
        entity = await self.bus_stop_repository.find_by_id(id, requested_fields)
        return self._entity_to_dto(entity)

    async def get_bus_stops_by_ids(self, ids: List[int]) -> List[BusStopOutputDTO]:
        """버스 정류장 여러 개 조회 - DataLoader용"""
        requested_fields = [
            "id",
            "name",
            "lat",
            "lng",
            "arrivals",
            "stop_bus_route_ids",
        ]
        entities = await self.bus_stop_repository.find_by_ids(ids, requested_fields)
        return [self._entity_to_dto(entity) for entity in entities]

    async def search_bus_stops(
        self,
        name: Optional[str],
        lat: Optional[float],
        lng: Optional[float],
        top_k: int,
    ) -> List[BusStopOutputDTO]:
        """버스 정류장 검색"""
        requested_fields = [
            "id",
            "name",
            "lat",
            "lng",
            "arrivals",
            "stop_bus_route_ids",
        ]
        entities = await self.bus_stop_repository.search_bus_stops(
            name, lat, lng, top_k, requested_fields
        )
        return [self._entity_to_dto(entity) for entity in entities]
