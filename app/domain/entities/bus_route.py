from dataclasses import dataclass
from typing import List, Optional

from app.domain.entities.entity_projection_factory import projection_factory


@dataclass(frozen=True)
class BusStopState:
    stop_ids: List[int]
    state: int
    first_car_time: str
    last_car_time: str
    car_number: int


@projection_factory
@dataclass(frozen=True)
class BusRouteEntity:
    id: int
    route_name: str
    type: int
    bus_stop_states: Optional[List[BusStopState]]
