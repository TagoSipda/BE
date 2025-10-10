import strawberry
from typing import List, Optional
from strawberry.types import Info

from app.adapter.inbound.graphql.resolvers.type.bus_route import BusRoute


@strawberry.type
class BusRouteQuery:
    """버스 노선 Query Resolver"""

    @strawberry.field
    async def bus_route(self, info: Info, id: int) -> Optional[BusRoute]:
        """버스 노선 단일 조회"""
        try:
            # UseCase 호출하여 DTO 받기
            bus_route_dto = await info.context.bus_route_use_case.get_bus_route(id)

            # DTO → GraphQL Type 변환
            return BusRoute.from_dto(bus_route_dto)
        except Exception as e:
            # TODO: 에러 처리 로직 추가
            raise e

    @strawberry.field
    async def search_bus_routes(
        self,
        info: Info,
        route_number: str,
        lat: Optional[float] = None,
        lng: Optional[float] = None,
    ) -> List[BusRoute]:
        """버스 노선 검색"""
        try:
            # UseCase 호출하여 DTO 리스트 받기
            bus_route_dtos = await info.context.bus_route_use_case.search_bus_routes(
                route_number=route_number, lat=lat, lng=lng
            )

            # DTO → GraphQL Type 변환
            return [BusRoute.from_dto(dto) for dto in bus_route_dtos]
        except Exception as e:
            # TODO: 에러 처리 로직 추가
            raise e
