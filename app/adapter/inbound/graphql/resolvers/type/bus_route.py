import strawberry
from typing import Optional, List, Annotated
from strawberry.types import Info

from app.application.interfaces.inbound.graphql.dto import (
    BusRouteOutputDTO,
    BusStopStateOutputDTO,
)


@strawberry.type
class BusStopState:
    """버스 정류장 상태 GraphQL Type"""

    stop_id: strawberry.Private[int]  # Field Resolver용 ID
    state: int  # 0: 버스 없음, 1: 여유, 2: 보통, 3: 혼잡, 4: 혼잡도 정보 없음
    first_car_time: str
    last_car_time: str
    car_number: int

    @strawberry.field
    async def stop(
        self, info: Info
    ) -> Annotated["BusStop", strawberry.lazy(".bus_stop")]:
        """ID를 실제 BusStop 객체로 변환 - DataLoader 사용"""
        bus_stop_dto = await info.context.bus_stop_loader.load(self.stop_id)
        # Lazy import to avoid circular dependency
        from app.adapter.inbound.graphql.resolvers.type.bus_stop import BusStop

        return BusStop.from_dto(bus_stop_dto)

    @classmethod
    def from_dto(cls, dto: BusStopStateOutputDTO) -> "BusStopState":
        """DTO → GraphQL Type 변환"""
        return cls(
            stop_id=dto.stop_id,
            state=dto.state,
            first_car_time=dto.first_car_time,
            last_car_time=dto.last_car_time,
            car_number=dto.car_number,
        )


@strawberry.type
class BusRoute:
    """버스 노선 GraphQL Type"""

    id: int
    route_name: str
    type: int  # 1: 일반버스, 2: 지선버스, 3: 간선버스, 4: 순환버스, 5: 마을버스, 6: 순환버스, 7: 급행버스, 8: 농어촌버스
    bus_stop_states: Optional[List[BusStopState]] = None

    @classmethod
    def from_dto(cls, dto: BusRouteOutputDTO) -> "BusRoute":
        """DTO → GraphQL Type 변환"""
        bus_stop_states = None
        if dto.bus_stop_states:
            bus_stop_states = [
                BusStopState.from_dto(state) for state in dto.bus_stop_states
            ]

        return cls(
            id=dto.id,
            route_name=dto.route_name,
            type=dto.type,
            bus_stop_states=bus_stop_states,
        )
