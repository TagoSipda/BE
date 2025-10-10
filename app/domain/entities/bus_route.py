from typing import List, Optional
from pydantic import BaseModel

from app.domain.entities.entity_base import Entity


class BusStopState(BaseModel):
    """버스 정류장 상태 (Value Object)"""

    stop_id: int  # 단일 정거장 ID
    state: int  # 0: 버스 없음, 1: 여유, 2: 보통, 3: 혼잡, 4: 혼잡도 정보 없음
    first_car_time: str  # 첫차 시간 (예: "7:46")
    last_car_time: str  # 막차 시간 (예: "23:13")
    car_number: int  # 버스 차량 번호, 차량이 현 위치에 없으면 0

    model_config = {"frozen": True}


class BusRouteEntity(Entity):
    """버스 노선 Entity 스키마"""

    id: int
    route_name: str
    type: int
    bus_stop_states: Optional[List[BusStopState]] = None


if __name__ == "__main__":
    data = {
        "id": 1,
        "route_name": "temp",
        "type": 1,
        "bus_stop_states": [
            {
                "stop_id": 123,
                "state": 1,
                "first_car_time": "10:00",
                "last_car_time": "22:00",
                "car_number": 1234,
            }
        ],
    }
    proj = BusRouteEntity.create_projection(
        data, ["id", "route_name", "type", "bus_stop_states"]
    )
    print(proj.model_dump())
