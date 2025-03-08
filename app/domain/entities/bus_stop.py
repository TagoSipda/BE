from dataclasses import dataclass
from typing import List, Optional

from app.domain.entities.entity_projection_factory import projection_factory


@projection_factory
@dataclass(frozen=True)
class BusStopEntity:
    id: int
    name: str
    lat: float
    lng: float
    arrivals: List[dict] = None
    stop_bus_route_ids: List[int] = None
