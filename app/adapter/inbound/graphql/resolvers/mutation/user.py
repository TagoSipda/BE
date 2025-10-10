import strawberry
from typing import Optional, List

from app.adapter.input.graphql.resolvers.type.user import (
    AuthPayload,
    User,
    UserConfig,
)
from app.adapter.input.graphql.resolvers.directive.auth import auth_resolver
from app.adapter.input.graphql.resolvers.input.user import UpdateUserConfigInput


@strawberry.type
class UserMutation:
    @strawberry.mutation(directives=[auth_resolver])
    def delete_user(self) -> bool:
        # TODO: 사용자 삭제 로직 구현
        return True

    @strawberry.mutation(directives=[auth_resolver])
    def set_folder_name(self, color: str, name: Optional[str]) -> bool:
        # TODO: 폴더 이름 설정 로직 구현
        return True

    @strawberry.mutation(directives=[auth_resolver])
    def add_bus_stop(self, color: str, bus_stop_id: int) -> bool:
        # TODO: 버스 정거장 추가 로직 구현
        return True

    @strawberry.mutation(directives=[auth_resolver])
    def add_bus_route(self, color: str, bus_stop_id: int, bus_route_id: int) -> bool:
        # TODO: 버스 노선 추가 로직 구현
        return True

    @strawberry.mutation(directives=[auth_resolver])
    def reorder_folder_bus_stop(self, color: str, reorder_sequence: List[int]) -> bool:
        # TODO: 폴더 내 정거장 순서 변경 로직 구현
        return True

    @strawberry.mutation(directives=[auth_resolver])
    def update_user_config(self, input: UpdateUserConfigInput) -> UserConfig:
        # TODO: 사용자 설정 업데이트 로직 구현
        return UserConfig(font_size=input.font_size or 1)
