import graphene


class BusArrivalInfoType(graphene.ObjectType):
    bus_route = graphene.Field(
        "app.interfaces.input.v1.graphql.resolvers.type.bus_route.BusRouteType",
        required=True,
    )
    next_bus_stop_name = graphene.String(required=True)
    first_estimated_arrival_time = graphene.Int(required=True)
    second_estimated_arrival_time = graphene.Int(required=True)
    first_remaining_stops = graphene.Int(required=True)
    second_remaining_stops = graphene.Int(required=True)
    first_congestion_level = graphene.Int()  # Optional
    second_congestion_level = graphene.Int()  # Optional
    first_remaining_seats = graphene.Int()  # Optional
    second_remaining_seats = graphene.Int()  # Optional


class BusStopType(graphene.ObjectType):
    id = graphene.Int(required=True)
    name = graphene.String(required=True)
    lat = graphene.Float(required=True)
    lng = graphene.Float(required=True)
    arrivals = graphene.NonNull(graphene.List(lambda: BusArrivalInfoType))
    stop_bus_routes = graphene.NonNull(
        graphene.List(
            "app.interfaces.input.v1.graphql.resolvers.type.bus_route.BusRouteType",
            required=True,
        )
    )
