import strawberry
from typing import List, Optional
from strawberry.types import Info

from app.adapter.inbound.graphql.resolvers.type.bus_stop import BusStop


@strawberry.type
class BusStopQuery:
    """버스 정류장 Query Resolver"""

    @strawberry.field
    async def bus_stop(self, info: Info, id: int) -> Optional[BusStop]:
        """버스 정류장 단일 조회"""
        try:
            # UseCase 호출하여 DTO 받기
            bus_stop_dto = await info.context.bus_stop_use_case.get_bus_stop(id)

            # DTO → GraphQL Type 변환
            return BusStop.from_dto(bus_stop_dto)
        except Exception as e:
            # TODO: 에러 처리 로직 추가
            raise e

    @strawberry.field
    async def search_bus_stops(
        self,
        info: Info,
        top_k: int,
        name: Optional[str] = None,
        lat: Optional[float] = None,
        lng: Optional[float] = None,
    ) -> List[BusStop]:
        """버스 정류장 검색"""
        # Validation: name 또는 (lat, lng) 중 하나 이상 필수
        if not name and (lat is None or lng is None):
            raise ValueError("name 또는 (lat, lng)가 필수입니다.")

        try:
            # UseCase 호출하여 DTO 리스트 받기
            bus_stop_dtos = await info.context.bus_stop_use_case.search_bus_stops(
                name=name, lat=lat, lng=lng, top_k=top_k
            )

            # DTO → GraphQL Type 변환
            return [BusStop.from_dto(dto) for dto in bus_stop_dtos]
        except Exception as e:
            # TODO: 에러 처리 로직 추가
            raise e
