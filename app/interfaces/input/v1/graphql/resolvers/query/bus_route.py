import strawberry
from typing import List, Optional
from app.interfaces.input.v1.graphql.resolvers.type.bus_route import BusRoute


@strawberry.type
class BusRouteQuery:
    @strawberry.field
    def bus_route(self, id: int) -> BusRoute:
        # 여기에 실제 데이터베이스 조회 로직 추가
        return BusRoute(id=id, route_name="Sample Route", type=1, bus_stop_states=[])

    @strawberry.field
    def search_bus_routes(
        self,
        route_number: str,
        lat: Optional[float] = None,
        lng: Optional[float] = None,
    ) -> List[BusRoute]:
        # 여기에 검색 로직 추가
        return [
            BusRoute(id=1, route_name="Sample Route", type=1, bus_stop_states=[]),
            BusRoute(id=2, route_name="Sample Route", type=1, bus_stop_states=[]),
        ]
