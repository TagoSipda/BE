import graphene

from app.interfaces.input.v1.graphql.resolvers.type.bus_stop import BusStopType


class BusStopQuery(graphene.ObjectType):
    bus_stop = graphene.Field(BusStopType, id=graphene.Int(required=True))
    search_bus_stops = graphene.List(
        BusStopType,
        name=graphene.String(),
        lat=graphene.Float(),
        lng=graphene.Float(),
        top_k=graphene.Int(required=True),
    )

    def resolve_bus_stop(self, info, id):
        # 여기에 실제 데이터베이스 조회 로직 추가
        return BusStopType(
            id=id,
            name="Sample Stop",
            lat=37.33,
            lng=126.12,
            arrivals=[],
            stop_bus_routes=[],
        )

    def resolve_search_bus_stops(self, info, name=None, lat=None, lng=None, top_k=5):
        # 여기에 검색 로직 추가
        return [
            BusStopType(
                id=id,
                name="Sample Stop",
                lat=37.33,
                lng=126.12,
                arrivals=[],
                stop_bus_routes=[],
            ),
            BusStopType(
                id=id,
                name="Sample Stop",
                lat=37.33,
                lng=126.12,
                arrivals=[],
                stop_bus_routes=[],
            ),
        ]
