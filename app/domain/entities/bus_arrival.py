from typing import Optional

from app.domain.entities.entity_base import Entity


class BusArrivalInfoEntity(Entity):
    """버스 도착 정보 Entity 스키마"""

    bus_route_id: int  # 순환 참조 방지를 위해 ID만 저장
    next_bus_stop_name: str  # 다음 정거장 이름 (어디 방향인지 표시)
    first_estimated_arrival_time: int  # 초 단위
    second_estimated_arrival_time: int  # 초 단위
    first_remaining_stops: int  # 3: 3번째 전, 0: AI 예측, -1: 정보 없음
    second_remaining_stops: int
    first_congestion_level: Optional[int] = (
        None  # 1: 여유, 2: 보통, 3: 혼잡, -1: 정보 없음
    )
    second_congestion_level: Optional[int] = None
    first_remaining_seats: Optional[int] = None  # -1: 정보없음
    second_remaining_seats: Optional[int] = None
