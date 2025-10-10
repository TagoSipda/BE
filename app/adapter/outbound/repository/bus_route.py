from typing import List
from pydantic import BaseModel

from app.application.interfaces.outbound.repository.bus_route import BusRouteRepository
from app.domain.entities.bus_route import BusRouteEntity


class BusRouteRepositoryImpl(BusRouteRepository):
    def find_by_id(self, id: int, requested_fields: List[str]) -> BaseModel:
        # 외부 API나 DB에서 데이터 가져옴 (임시 데이터)
        data = {"id": id, "route_name": "temp", "type": 1, "bus_stop_states": None}

        # Entity 스키마를 사용해 Projection 생성
        return BusRouteEntity.create_projection(data, requested_fields)

    def search_bus_routes(
        self, name: str, lat: float, lng: float, top_k: int, requested_fields: List[str]
    ) -> List[BaseModel]:
        pass
