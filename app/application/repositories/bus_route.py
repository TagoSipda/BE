from abc import ABC, abstractmethod
from typing import Optional, List

from app.domain.entities.bus_route import BusRouteEntityProjection


class BusRouteRepository(ABC):
    @abstractmethod
    def find_by_id(id: int, requested_fields: List[str]) -> BusRouteEntityProjection:
        pass

    @abstractmethod
    def search_bus_routes(
        name: Optional[str],
        lat: Optional[str],
        lng: Optional[str],
        top_k: int,
        requested_fields: List[str],
    ) -> List[BusRouteEntityProjection]:
        pass
