import strawberry
from typing import Optional, List, Annotated


@strawberry.type
class BusArrivalInfo:
    bus_route: Annotated[
        "BusRoute",
        strawberry.lazy(".bus_route"),
    ]
    next_bus_stop_name: str
    first_estimated_arrival_time: int
    second_estimated_arrival_time: int
    first_remaining_stops: int
    second_remaining_stops: int
    first_congestion_level: Optional[int] = None  # Optional
    second_congestion_level: Optional[int] = None  # Optional
    first_remaining_seats: Optional[int] = None  # Optional
    second_remaining_seats: Optional[int] = None  # Optional


@strawberry.type
class BusStop:
    id: int
    name: str
    lat: float
    lng: float
    arrivals: List[BusArrivalInfo]
    stop_bus_routes: List[
        Annotated[
            "BusRoute",
            strawberry.lazy(".bus_route"),
        ]
    ]
