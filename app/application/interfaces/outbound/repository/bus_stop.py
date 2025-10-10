from abc import ABC, abstractmethod
from typing import Optional, List
from app.domain.entities.bus_stop import BusStopEntity


class BusStopRepository(ABC):
    @abstractmethod
    async def find_by_id(self, id: int, requested_fields: List[str]) -> BusStopEntity:
        """버스 정류장 조회 - Entity Projection 반환"""
        pass

    @abstractmethod
    async def find_by_ids(
        self, ids: List[int], requested_fields: List[str]
    ) -> List[BusStopEntity]:
        """버스 정류장 여러 개 조회 - DataLoader용"""
        pass

    @abstractmethod
    async def search_bus_stops(
        self,
        name: Optional[str],
        lat: Optional[float],
        lng: Optional[float],
        top_k: int,
        requested_fields: List[str],
    ) -> List[BusStopEntity]:
        """버스 정류장 검색 - Entity Projection 리스트 반환"""
        pass
