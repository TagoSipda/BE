import strawberry
from app.interfaces.input.v1.graphql.resolvers.type.user import User, UserConfig


@strawberry.type
class UserQuery:
    @strawberry.field
    def user(self) -> User:
        # 여기에 실제 JWT 파싱 로직 추가
        return User(
            id="1",
            provider="kakao",
            user_config=UserConfig(font_size=1),
        )
