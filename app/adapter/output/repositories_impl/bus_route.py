from typing import List

from app.application.repositories.bus_route import BusRouteRepository
from app.domain.entities.bus_route import BusRouteEntityProjection


class BusRouteRepositoryImpl(BusRouteRepository):
    def find_by_id(
        self, id: int, requested_fields: List[str]
    ) -> BusRouteEntityProjection:
        return BusRouteEntityProjection(
            id=id, name="temp", lat=10, lng=10, arrivals=[], stop_bus_route_ids=[]
        )

    def search_bus_routes(
        self, name: str, lat: float, lng: float, top_k: int, requested_fields: List[str]
    ) -> List[BusRouteEntityProjection]:
        pass
