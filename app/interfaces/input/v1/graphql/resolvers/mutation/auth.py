import strawberry

from app.interfaces.input.v1.graphql.resolvers.type.user import (
    AuthPayload,
    User,
    UserConfig,
)
from app.interfaces.input.v1.graphql.resolvers.directive.auth import auth_resolver


@strawberry.type
class AuthMutation:
    @strawberry.mutation
    def login(self, provider: str, social_token: str) -> AuthPayload:
        # 소셜 로그인 로직 구현
        return AuthPayload(
            access_token="sample_access_token",
            refresh_token="sample_refresh_token",
            user=User(
                id="123",
                username="sample_user",
                email="sample@example.com",
                profile_picture=None,
                provider=provider,
                user_config=UserConfig(font_size=2),
                user_bookmarks=[],
            ),
        )

    @strawberry.mutation(directives=[auth_resolver])
    def logout(self) -> bool:
        # 로그아웃 로직 구현
        return True

    @strawberry.mutation
    def refresh_access_token(self, refresh_token: str) -> AuthPayload:
        # AccessToken 갱신 로직 구현
        return AuthPayload(
            access_token="new_access_token",
            refresh_token=refresh_token,
            user=User(
                id="123",
                username="sample_user",
                email="sample@example.com",
                profile_picture=None,
                provider="google",
                user_config=UserConfig(font_size=2),
                user_bookmarks=[],
            ),
        )
