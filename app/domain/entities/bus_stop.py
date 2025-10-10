from typing import List, Optional

from app.domain.entities.entity_base import Entity
from app.domain.entities.bus_arrival import BusArrivalInfoEntity


class BusStopEntity(Entity):
    """버스 정류장 Entity 스키마"""

    id: int
    name: str
    lat: float
    lng: float
    arrivals: Optional[List[BusArrivalInfoEntity]] = None
    stop_bus_route_ids: Optional[List[int]] = None


if __name__ == "__main__":
    data = {
        "id": 1,
        "name": "강남역",
        "lat": 37.497952,
        "lng": 127.027619,
        # "arrivals": [{"bus": "146", "time": 300}],
        "stop_bus_route_ids": [1, 2, 3],
    }
    proj = BusStopEntity.create_projection(data, ["id", "name", "lat", "lng"])
    print(proj.model_dump())
