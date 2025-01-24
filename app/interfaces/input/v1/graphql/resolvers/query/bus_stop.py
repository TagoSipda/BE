import strawberry
from typing import List, Optional
from app.interfaces.input.v1.graphql.resolvers.type.bus_stop import BusStop


@strawberry.type
class BusStopQuery:
    @strawberry.field
    def bus_stop(self, id: int) -> BusStop:
        # 여기에 실제 데이터베이스 조회 로직 추가
        return BusStop(
            id=id,
            name="Sample Stop",
            lat=37.33,
            lng=126.12,
            arrivals=[],
            stop_bus_routes=[],
        )

    @strawberry.field
    def search_bus_stops(
        self,
        name: Optional[str] = None,
        lat: Optional[float] = None,
        lng: Optional[float] = None,
        top_k: int = 5,
    ) -> List[BusStop]:
        # 여기에 검색 로직 추가
        return [
            BusStop(
                id=1,
                name="Sample Stop",
                lat=37.33,
                lng=126.12,
                arrivals=[],
                stop_bus_routes=[],
            ),
            BusStop(
                id=2,
                name="Sample Stop",
                lat=37.33,
                lng=126.12,
                arrivals=[],
                stop_bus_routes=[],
            ),
        ]
