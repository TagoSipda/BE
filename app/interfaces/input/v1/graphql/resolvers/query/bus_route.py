import graphene

from app.interfaces.input.v1.graphql.resolvers.type.bus_route import BusRouteType


class BusRouteQuery(graphene.ObjectType):
    bus_route = graphene.Field(BusRouteType, id=graphene.Int(required=True))
    search_bus_routes = graphene.List(
        BusRouteType,
        route_number=graphene.String(required=True),
        lat=graphene.Float(),
        lng=graphene.Float(),
    )

    def resolve_bus_route(self, info, id):
        # 여기에 실제 데이터베이스 조회 로직 추가
        return BusRouteType(
            id=id, route_name="Sample Route", type=1, bus_stop_states=[]
        )

    def resolve_search_bus_routes(self, info, route_number, lat=None, lng=None):
        # 여기에 검색 로직 추가
        return [
            BusRouteType(id=1, route_name="Sample Route", type=1, bus_stop_states=[]),
            BusRouteType(id=2, route_name="Sample Route", type=1, bus_stop_states=[]),
        ]
