import strawberry
from typing import Optional, List, Annotated
from strawberry.types import Info

from app.application.interfaces.inbound.graphql.dto import (
    UserOutputDTO,
    UserConfigOutputDTO,
    BookmarkOutputDTO,
    FolderOutputDTO,
    BusStopBusPairOutputDTO,
    AuthPayloadOutputDTO,
    SocialProviderDTO,
    FolderColorDTO,
)


@strawberry.type
class UserConfig:
    """사용자 설정 GraphQL Type"""

    font_size: int  # 1: small, 2: medium, 3: large

    @classmethod
    def from_dto(cls, dto: UserConfigOutputDTO) -> "UserConfig":
        """DTO → GraphQL Type 변환"""
        return cls(font_size=dto.font_size)


@strawberry.type
class BusStopBusPair:
    """버스 정류장-버스 노선 쌍 GraphQL Type"""

    bus_stop_id: strawberry.Private[int]  # Field Resolver용 ID
    bus_route_ids: strawberry.Private[List[int]]  # Field Resolver용 ID

    @strawberry.field
    async def bus_stop(
        self, info: Info
    ) -> Annotated["BusStop", strawberry.lazy(".bus_stop")]:
        """ID를 실제 BusStop 객체로 변환 - DataLoader 사용"""
        bus_stop_dto = await info.context.bus_stop_loader.load(self.bus_stop_id)
        from app.adapter.inbound.graphql.resolvers.type.bus_stop import BusStop

        return BusStop.from_dto(bus_stop_dto)

    @strawberry.field
    async def buses(
        self, info: Info
    ) -> List[Annotated["BusRoute", strawberry.lazy(".bus_route")]]:
        """ID 리스트를 실제 BusRoute 객체 리스트로 변환 - DataLoader 사용"""
        if not self.bus_route_ids:
            return []

        bus_route_dtos = await info.context.bus_route_loader.load_many(
            self.bus_route_ids
        )
        from app.adapter.inbound.graphql.resolvers.type.bus_route import BusRoute

        return [BusRoute.from_dto(dto) for dto in bus_route_dtos if dto is not None]

    @classmethod
    def from_dto(cls, dto: BusStopBusPairOutputDTO) -> "BusStopBusPair":
        """DTO → GraphQL Type 변환"""
        return cls(
            bus_stop_id=dto.bus_stop_id,
            bus_route_ids=dto.bus_route_ids,
        )


@strawberry.type
class Bookmark:
    """북마크 GraphQL Type"""

    id: int
    pairs: Optional[List[BusStopBusPair]] = None

    @classmethod
    def from_dto(cls, dto: BookmarkOutputDTO) -> "Bookmark":
        """DTO → GraphQL Type 변환"""
        pairs = None
        if dto.pairs:
            pairs = [BusStopBusPair.from_dto(pair) for pair in dto.pairs]

        return cls(id=dto.id, pairs=pairs)


@strawberry.type
class Folder:
    """폴더 GraphQL Type"""

    name: Optional[str] = None
    color: str
    bookmark_ids: strawberry.Private[Optional[List[int]]] = None  # Field Resolver용

    @strawberry.field
    async def bookmark(self, info: Info) -> Optional[List[Bookmark]]:
        """ID 리스트를 실제 Bookmark 객체 리스트로 변환"""
        if not self.bookmark_ids:
            return None

        # TODO: Bookmark UseCase와 DataLoader 구현 필요
        # bookmark_dtos = await info.context.bookmark_loader.load_many(self.bookmark_ids)
        # return [Bookmark.from_dto(dto) for dto in bookmark_dtos if dto is not None]
        return None

    @classmethod
    def from_dto(cls, dto: FolderOutputDTO) -> "Folder":
        """DTO → GraphQL Type 변환"""
        return cls(
            name=dto.name,
            color=dto.color.value,
            bookmark_ids=dto.bookmark_ids,
        )


@strawberry.type
class User:
    """사용자 GraphQL Type"""

    id: str
    username: Optional[str] = None
    email: Optional[str] = None
    profile_picture: Optional[str] = None
    provider: str
    user_config: UserConfig
    bookmark_ids: strawberry.Private[Optional[List[int]]] = None  # Field Resolver용

    @strawberry.field
    async def user_bookmarks(self, info: Info) -> Optional[List[Bookmark]]:
        """ID 리스트를 실제 Bookmark 객체 리스트로 변환"""
        if not self.bookmark_ids:
            return None

        # TODO: Bookmark UseCase와 DataLoader 구현 필요
        # bookmark_dtos = await info.context.bookmark_loader.load_many(self.bookmark_ids)
        # return [Bookmark.from_dto(dto) for dto in bookmark_dtos if dto is not None]
        return None

    @classmethod
    def from_dto(cls, dto: UserOutputDTO) -> "User":
        """DTO → GraphQL Type 변환"""
        return cls(
            id=dto.id,
            username=dto.username,
            email=dto.email,
            profile_picture=dto.profile_picture,
            provider=dto.provider.value,
            user_config=UserConfig.from_dto(dto.user_config),
            bookmark_ids=dto.bookmark_ids,
        )


@strawberry.type
class AuthPayload:
    """인증 페이로드 GraphQL Type"""

    access_token: str
    refresh_token: str
    user: User

    @classmethod
    def from_dto(cls, dto: AuthPayloadOutputDTO) -> "AuthPayload":
        """DTO → GraphQL Type 변환"""
        return cls(
            access_token=dto.access_token,
            refresh_token=dto.refresh_token,
            user=User.from_dto(dto.user),
        )
