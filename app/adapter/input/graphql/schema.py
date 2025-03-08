import strawberry

from app.adapter.input.graphql.resolvers.query.bus_stop import BusStopQuery
from app.adapter.input.graphql.resolvers.query.bus_route import BusRouteQuery
from app.adapter.input.graphql.resolvers.query.user import UserQuery

from app.adapter.input.graphql.resolvers.mutation.auth import AuthMutation
from app.adapter.input.graphql.resolvers.mutation.user import UserMutation


@strawberry.type
class Query(BusStopQuery, BusRouteQuery, UserQuery):

    pass


@strawberry.type
class Mutation(AuthMutation, UserMutation):

    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
