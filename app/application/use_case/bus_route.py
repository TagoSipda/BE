from typing import List, Optional
from app.application.interfaces.outbound.repository.bus_route import BusRouteRepository
from app.application.interfaces.inbound.graphql.dto import (
    BusRouteOutputDTO,
    BusStopStateOutputDTO,
)
from app.domain.entities.bus_route import BusRouteEntity


class BusRouteUseCaseImpl:
    """버스 노선 UseCase 구현체"""

    def __init__(self, bus_route_repository: BusRouteRepository):
        self.bus_route_repository = bus_route_repository

    def _entity_to_dto(self, entity: BusRouteEntity) -> BusRouteOutputDTO:
        """BusRouteEntity를 BusRouteOutputDTO로 변환"""
        # bus_stop_states 변환
        bus_stop_states_dto = None
        if hasattr(entity, "bus_stop_states") and entity.bus_stop_states is not None:
            bus_stop_states_dto = [
                BusStopStateOutputDTO(
                    stop_id=state.stop_id,
                    state=state.state,
                    first_car_time=state.first_car_time,
                    last_car_time=state.last_car_time,
                    car_number=state.car_number,
                )
                for state in entity.bus_stop_states
            ]

        return BusRouteOutputDTO(
            id=entity.id,
            route_name=entity.route_name,
            type=entity.type,
            bus_stop_states=bus_stop_states_dto,
        )

    async def get_bus_route(self, id: int) -> BusRouteOutputDTO:
        """버스 노선 조회"""
        requested_fields = ["id", "route_name", "type", "bus_stop_states"]
        entity = await self.bus_route_repository.find_by_id(id, requested_fields)
        return self._entity_to_dto(entity)

    async def get_bus_routes_by_ids(self, ids: List[int]) -> List[BusRouteOutputDTO]:
        """버스 노선 여러 개 조회 - DataLoader용"""
        requested_fields = ["id", "route_name", "type", "bus_stop_states"]
        entities = await self.bus_route_repository.find_by_ids(ids, requested_fields)
        return [self._entity_to_dto(entity) for entity in entities]

    async def search_bus_routes(
        self,
        route_number: str,
        lat: Optional[float],
        lng: Optional[float],
    ) -> List[BusRouteOutputDTO]:
        """버스 노선 검색"""
        requested_fields = ["id", "route_name", "type", "bus_stop_states"]
        entities = await self.bus_route_repository.search_bus_routes(
            route_number, lat, lng, requested_fields
        )
        return [self._entity_to_dto(entity) for entity in entities]
