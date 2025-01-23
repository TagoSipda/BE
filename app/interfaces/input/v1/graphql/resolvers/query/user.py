import graphene

from app.interfaces.input.v1.graphql.resolvers.type.user import UserType, UserConfigType


class UserQuery(graphene.ObjectType):
    user = graphene.Field(UserType)

    def resolve_user(self, info):
        # 여기에 실제 JWT 파싱 로직 추가
        return UserType(
            id="1",
            provider="kakao",
            user_config=UserConfigType(font_size=1),
        )
