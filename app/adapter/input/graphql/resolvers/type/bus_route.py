import strawberry
from typing import Optional, Annotated


@strawberry.type
class BusStopState:
    stop: Annotated["BusStop", strawberry.lazy(".bus_stop")]
    state: int
    first_car_time: str
    last_car_time: str
    car_number: int


@strawberry.type
class BusRoute:
    id: int
    route_name: str
    type: int  # 버스 타입
    bus_stop_states: Optional[list[BusStopState]]
