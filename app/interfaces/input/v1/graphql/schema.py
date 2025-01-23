import graphene
from app.interfaces.input.v1.graphql.resolvers.query.bus_stop import BusStopQuery
from app.interfaces.input.v1.graphql.resolvers.query.bus_route import BusRouteQuery

# from app.interfaces.input.v1.graphql.resolvers.query.auth import UserQuery

# from app.interfaces.input.v1.graphql.resolvers.mutation.auth import AuthMutation
# from app.interfaces.input.v1.graphql.resolvers.mutation.user import UserMutation
# from app.interfaces.input.v1.graphql.resolvers.mutation.folder import FolderMutation


class Query(BusStopQuery, BusRouteQuery, graphene.ObjectType):
    """Query Root - 모든 쿼리를 통합"""

    pass


# class Mutation(AuthMutation, UserMutation, FolderMutation, graphene.ObjectType):
#     """Mutation Root - 모든 뮤테이션을 통합"""

#     pass


# 스키마 정의
schema = graphene.Schema(query=Query)
# schema = graphene.Schema(query=Query, mutation=Mutation)
