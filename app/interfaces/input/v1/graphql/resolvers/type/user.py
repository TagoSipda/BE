import graphene

from app.interfaces.input.v1.graphql.resolvers.type.bus_stop import BusStopType
from app.interfaces.input.v1.graphql.resolvers.type.bus_route import BusRouteType


class UserConfigType(graphene.ObjectType):
    font_size = graphene.Int(required=True)  # 1: small, 2: medium, 3: large


class BusStopBusPairType(graphene.ObjectType):
    bus_stop = graphene.Field(lambda: BusStopType, required=True)
    buses = graphene.List(lambda: graphene.NonNull(BusRouteType))


class BookmarkType(graphene.ObjectType):
    id = graphene.Int(required=True)
    pairs = graphene.List(lambda: graphene.NonNull(BusStopBusPairType))


class FolderType(graphene.ObjectType):
    name = graphene.String()
    color = graphene.String(required=True)
    bookmark = graphene.List(lambda: graphene.NonNull(BookmarkType))


class UserType(graphene.ObjectType):
    id = graphene.String(required=True)
    username = graphene.String()
    email = graphene.String()
    profile_picture = graphene.String()
    provider = graphene.String(
        required=True
    )  # 소셜 로그인 공급자 (예: "kakao", "google", "facebook")
    user_config = graphene.Field(UserConfigType, required=True)
    user_bookmarks = graphene.List(lambda: BookmarkType)


class AuthPayloadType(graphene.ObjectType):
    access_token = graphene.String(required=True)
    refresh_token = graphene.String(required=True)
    user = graphene.Field(UserType, required=True)
