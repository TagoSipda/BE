from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from app.domain.entities.entity_base import Entity


class FolderColor(str, Enum):
    """고정된 폴더 색상"""

    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"


class BusStopBusPairEntity(BaseModel):
    """버스 정류장-버스 노선 쌍 (Value Object)"""

    bus_stop_id: int  # 순환 참조 방지
    bus_route_ids: List[int]  # 순환 참조 방지

    model_config = {"frozen": True}


class BookmarkEntity(Entity):
    """북마크 Entity 스키마"""

    id: int
    pairs: Optional[List[BusStopBusPairEntity]] = None


class FolderEntity(Entity):
    """폴더 Entity 스키마"""

    name: Optional[str] = None
    color: FolderColor  # Enum으로 고정된 색상만 허용
    bookmark_ids: Optional[List[int]] = None  # 순환 참조 방지
