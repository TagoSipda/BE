from enum import Enum
from typing import List, Optional

from app.domain.entities.entity_base import Entity


class SocialProvider(str, Enum):
    """소셜 로그인 제공자"""

    KAKAO = "kakao"
    GOOGLE = "google"
    FACEBOOK = "facebook"


class UserConfigEntity(Entity):
    """사용자 설정 Entity 스키마"""

    font_size: int  # 1: small, 2: medium, 3: large


class UserEntity(Entity):
    """사용자 Entity 스키마"""

    id: str
    username: Optional[str] = None
    email: Optional[str] = None
    profile_picture: Optional[str] = None
    provider: SocialProvider  # 소셜 로그인 공급자
    user_config: UserConfigEntity
    bookmark_ids: Optional[List[int]] = None  # 순환 참조 방지
