from app.domain.entities.entity_base import Entity
from app.domain.entities.user import UserEntity


class AuthPayloadEntity(Entity):
    """인증 결과 Entity 스키마"""

    access_token: str
    refresh_token: str
    user: UserEntity
