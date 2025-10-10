"""도메인 Entity 모듈

모든 Entity를 중앙에서 관리하여 import 편의성을 제공합니다.
"""

from app.domain.entities.auth import AuthPayloadEntity
from app.domain.entities.bookmark import (
    BookmarkEntity,
    BusStopBusPairEntity,
    FolderColor,
    FolderEntity,
)
from app.domain.entities.bus_arrival import BusArrivalInfoEntity
from app.domain.entities.bus_route import BusRouteEntity, BusStopState
from app.domain.entities.bus_stop import BusStopEntity
from app.domain.entities.entity_base import Entity
from app.domain.entities.user import SocialProvider, UserConfigEntity, UserEntity

__all__ = [
    # Base
    "Entity",
    # Bus
    "BusStopEntity",
    "BusRouteEntity",
    "BusStopState",
    "BusArrivalInfoEntity",
    # User & Auth
    "UserEntity",
    "UserConfigEntity",
    "SocialProvider",
    "AuthPayloadEntity",
    # Bookmark
    "BookmarkEntity",
    "FolderEntity",
    "BusStopBusPairEntity",
    "FolderColor",
]
