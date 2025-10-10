import strawberry
from typing import Optional, List, Annotated
from strawberry.types import Info

from app.application.interfaces.inbound.graphql.dto import (
    BusStopOutputDTO,
    BusArrivalInfoOutputDTO,
)


@strawberry.type
class BusArrivalInfo:
    """버스 도착 정보 GraphQL Type"""

    bus_route_id: strawberry.Private[int]  # Field Resolver용 ID
    next_bus_stop_name: str
    first_estimated_arrival_time: int
    second_estimated_arrival_time: int
    first_remaining_stops: int
    second_remaining_stops: int
    first_congestion_level: Optional[int] = None
    second_congestion_level: Optional[int] = None
    first_remaining_seats: Optional[int] = None
    second_remaining_seats: Optional[int] = None

    @strawberry.field
    async def bus_route(
        self, info: Info
    ) -> Annotated["BusRoute", strawberry.lazy(".bus_route")]:
        """ID를 실제 BusRoute 객체로 변환 - DataLoader 사용"""
        bus_route_dto = await info.context.bus_route_loader.load(self.bus_route_id)
        # Lazy import to avoid circular dependency
        from app.adapter.inbound.graphql.resolvers.type.bus_route import BusRoute

        return BusRoute.from_dto(bus_route_dto)

    @classmethod
    def from_dto(cls, dto: BusArrivalInfoOutputDTO) -> "BusArrivalInfo":
        """DTO → GraphQL Type 변환"""
        return cls(
            bus_route_id=dto.bus_route_id,
            next_bus_stop_name=dto.next_bus_stop_name,
            first_estimated_arrival_time=dto.first_estimated_arrival_time,
            second_estimated_arrival_time=dto.second_estimated_arrival_time,
            first_remaining_stops=dto.first_remaining_stops,
            second_remaining_stops=dto.second_remaining_stops,
            first_congestion_level=dto.first_congestion_level,
            second_congestion_level=dto.second_congestion_level,
            first_remaining_seats=dto.first_remaining_seats,
            second_remaining_seats=dto.second_remaining_seats,
        )


@strawberry.type
class BusStop:
    """버스 정류장 GraphQL Type"""

    id: int
    name: str
    lat: float
    lng: float
    arrivals: Optional[List[BusArrivalInfo]] = None
    stop_bus_route_ids: strawberry.Private[Optional[List[int]]] = (
        None  # Field Resolver용
    )

    @strawberry.field
    async def stop_bus_routes(
        self, info: Info
    ) -> List[Annotated["BusRoute", strawberry.lazy(".bus_route")]]:
        """ID 리스트를 실제 BusRoute 객체 리스트로 변환 - DataLoader 사용"""
        if not self.stop_bus_route_ids:
            return []

        # DataLoader로 한 번에 조회
        bus_route_dtos = await info.context.bus_route_loader.load_many(
            self.stop_bus_route_ids
        )

        # Lazy import to avoid circular dependency
        from app.adapter.inbound.graphql.resolvers.type.bus_route import BusRoute

        return [BusRoute.from_dto(dto) for dto in bus_route_dtos if dto is not None]

    @classmethod
    def from_dto(cls, dto: BusStopOutputDTO) -> "BusStop":
        """DTO → GraphQL Type 변환"""
        arrivals = None
        if dto.arrivals:
            arrivals = [BusArrivalInfo.from_dto(arr) for arr in dto.arrivals]

        return cls(
            id=dto.id,
            name=dto.name,
            lat=dto.lat,
            lng=dto.lng,
            arrivals=arrivals,
            stop_bus_route_ids=dto.stop_bus_route_ids,
        )
