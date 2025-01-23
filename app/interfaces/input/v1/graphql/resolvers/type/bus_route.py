import graphene

from app.interfaces.input.v1.graphql.resolvers.type.bus_stop import BusStopType


class BusStopStateType(graphene.ObjectType):
    stop = graphene.Field(lambda: BusStopType, required=True)
    state = graphene.Int(required=True)
    first_car_time = graphene.String(required=True)
    last_car_time = graphene.String(required=True)
    car_number = graphene.Int(required=True)


class BusRouteType(graphene.ObjectType):
    id = graphene.Int(required=True)
    route_name = graphene.String(required=True)
    type = graphene.Int(required=True)  # 버스 타입
    bus_stop_states = graphene.List(lambda: BusStopStateType)
