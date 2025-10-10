from abc import ABC, abstractmethod
from typing import Optional, List
from app.domain.entities.bus_route import BusRouteEntity


class BusRouteRepository(ABC):
    @abstractmethod
    async def find_by_id(self, id: int, requested_fields: List[str]) -> BusRouteEntity:
        """버스 노선 조회 - Entity Projection 반환"""
        pass

    @abstractmethod
    async def find_by_ids(
        self, ids: List[int], requested_fields: List[str]
    ) -> List[BusRouteEntity]:
        """버스 노선 여러 개 조회 - DataLoader용"""
        pass

    @abstractmethod
    async def search_bus_routes(
        self,
        route_number: str,
        lat: Optional[float],
        lng: Optional[float],
        requested_fields: List[str],
    ) -> List[BusRouteEntity]:
        """버스 노선 검색 - Entity Projection 리스트 반환"""
        pass
