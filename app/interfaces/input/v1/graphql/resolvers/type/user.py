import strawberry
from typing import Optional, List, Annotated


@strawberry.type
class UserConfig:
    font_size: int  # 1: small, 2: medium, 3: large


@strawberry.type
class BusStopBusPair:
    bus_stop: Annotated["BusStop", strawberry.lazy(".bus_stop")]
    buses: Optional[
        List[
            Annotated[
                "BusRoute",
                strawberry.lazy(".bus_route"),
            ]
        ]
    ]


@strawberry.type
class Bookmark:
    id: int
    pairs: List[BusStopBusPair]


@strawberry.type
class Folder:
    name: Optional[str]
    color: str
    bookmark: Optional[List[Bookmark]]


@strawberry.type
class User:
    id: str
    username: Optional[str]
    email: Optional[str]
    profile_picture: Optional[str]
    provider: str  # 소셜 로그인 공급자 (예: "kakao", "google", "facebook")
    user_config: UserConfig
    user_bookmarks: Optional[List[Bookmark]]


@strawberry.type
class AuthPayload:
    access_token: str
    refresh_token: str
    user: User
