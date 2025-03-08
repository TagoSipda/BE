from abc import ABC, abstractmethod
from typing import Optional, List

from app.domain.entities.bus_stop import BusStopEntityProjection


class BusStopRepository(ABC):
    @abstractmethod
    def find_by_id(id: int, requested_fields: List[str]) -> BusStopEntityProjection:
        pass

    @abstractmethod
    def search_bus_stops(
        name: Optional[str],
        lat: Optional[str],
        lng: Optional[str],
        top_k: int,
        requested_fields: List[str],
    ) -> List[BusStopEntityProjection]:
        pass
