from typing import List

from app.application.repositories.bus_stop import BusStopRepository
from app.domain.entities.bus_stop import BusStopEntityProjection


class BusStopRepositoryImpl(BusStopRepository):
    def find_by_id(
        self, id: int, requested_fields: List[str]
    ) -> BusStopEntityProjection:
        return BusStopEntityProjection(
            id=id, name="temp", lat=10, lng=10, arrivals=[], stop_bus_route_ids=[]
        )

    def search_bus_stops(
        self, name: str, lat: float, lng: float, top_k: int, requested_fields: List[str]
    ) -> List[BusStopEntityProjection]:
        pass
