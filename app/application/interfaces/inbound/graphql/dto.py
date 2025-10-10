"""GraphQL Inbound용 DTO (Data Transfer Object)

이 모듈은 프레임워크 독립적인 Input/Output DTO를 정의합니다.
- Pydantic BaseModel 사용
- snake_case 네이밍 (GraphQL에서는 auto_camel_case로 자동 변환)
- 순환 참조 방지를 위해 ID만 참조
"""

from typing import List, Optional
from pydantic import BaseModel
from enum import Enum


# =========================
# Enums
# =========================


class SocialProviderDTO(str, Enum):
    """소셜 로그인 제공자"""

    KAKAO = "kakao"
    GOOGLE = "google"
    FACEBOOK = "facebook"


class FolderColorDTO(str, Enum):
    """폴더 색상"""

    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"


# =========================
# Output DTOs - Bus Related
# =========================


class BusStopStateOutputDTO(BaseModel):
    """버스 정류장 상태 Output DTO"""

    stop_id: int
    state: int  # 0: 버스 없음, 1: 여유, 2: 보통, 3: 혼잡, 4: 혼잡도 정보 없음
    first_car_time: str  # 예: "7:46"
    last_car_time: str  # 예: "23:13"
    car_number: int  # 버스 차량 번호, 차량이 현 위치에 없으면 0


class BusRouteOutputDTO(BaseModel):
    """버스 노선 Output DTO"""

    id: int
    route_name: str
    type: int  # 1: 일반버스, 2: 지선버스, 3: 간선버스, 4: 순환버스, 5: 마을버스, 6: 순환버스, 7: 급행버스, 8: 농어촌버스
    bus_stop_states: Optional[List[BusStopStateOutputDTO]] = None


class BusArrivalInfoOutputDTO(BaseModel):
    """버스 도착 정보 Output DTO"""

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


class BusStopOutputDTO(BaseModel):
    """버스 정류장 Output DTO"""

    id: int
    name: str
    lat: float
    lng: float
    arrivals: Optional[List[BusArrivalInfoOutputDTO]] = None
    stop_bus_route_ids: Optional[List[int]] = None  # Field Resolver에서 해결


# =========================
# Output DTOs - User Related
# =========================


class UserConfigOutputDTO(BaseModel):
    """사용자 설정 Output DTO"""

    font_size: int  # 1: small, 2: medium, 3: large


class BusStopBusPairOutputDTO(BaseModel):
    """버스 정류장-버스 노선 쌍 Output DTO"""

    bus_stop_id: int
    bus_route_ids: List[int]


class BookmarkOutputDTO(BaseModel):
    """북마크 Output DTO"""

    id: int
    pairs: Optional[List[BusStopBusPairOutputDTO]] = None


class FolderOutputDTO(BaseModel):
    """폴더 Output DTO"""

    name: Optional[str] = None
    color: FolderColorDTO
    bookmark_ids: Optional[List[int]] = None  # Field Resolver에서 해결


class UserOutputDTO(BaseModel):
    """사용자 Output DTO"""

    id: str
    username: Optional[str] = None
    email: Optional[str] = None
    profile_picture: Optional[str] = None
    provider: SocialProviderDTO
    user_config: UserConfigOutputDTO
    bookmark_ids: Optional[List[int]] = None  # Field Resolver에서 해결


class AuthPayloadOutputDTO(BaseModel):
    """인증 페이로드 Output DTO"""

    access_token: str
    refresh_token: str
    user: UserOutputDTO


# =========================
# Input DTOs
# =========================


class LoginInputDTO(BaseModel):
    """로그인 Input DTO"""

    provider: str
    social_token: str


class UpdateUserConfigInputDTO(BaseModel):
    """사용자 설정 수정 Input DTO"""

    font_size: Optional[int] = None


class SetFolderNameInputDTO(BaseModel):
    """폴더 이름 설정 Input DTO"""

    color: str
    name: Optional[str] = None


class AddBusStopInputDTO(BaseModel):
    """버스 정류장 추가 Input DTO"""

    color: str
    bus_stop_id: int


class AddBusRouteInputDTO(BaseModel):
    """버스 노선 추가 Input DTO"""

    color: str
    bus_stop_id: int
    bus_route_id: int


class ReorderFolderBusStopInputDTO(BaseModel):
    """폴더 버스 정류장 재정렬 Input DTO"""

    color: str
    reorder_sequence: List[int]


class SearchBusStopsInputDTO(BaseModel):
    """버스 정류장 검색 Input DTO"""

    name: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    top_k: int


class SearchBusRoutesInputDTO(BaseModel):
    """버스 노선 검색 Input DTO"""

    route_number: str
    lat: Optional[float] = None
    lng: Optional[float] = None
