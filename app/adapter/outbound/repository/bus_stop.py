from typing import List
from pydantic import BaseModel

from app.application.interfaces.outbound.repository.bus_stop import BusStopRepository
from app.domain.entities.bus_stop import BusStopEntity


class BusStopRepositoryImpl(BusStopRepository):
    def find_by_id(self, id: int, requested_fields: List[str]) -> BaseModel:
        # 외부 API나 DB에서 데이터 가져옴 (임시 데이터)
        data = {
            "id": id,
            "name": "temp",
            "lat": 10.0,
            "lng": 10.0,
            "arrivals": [],
            "stop_bus_route_ids": [],
        }

        # Entity 스키마를 사용해 Projection 생성
        return BusStopEntity.create_projection(data, requested_fields)

    def search_bus_stops(
        self, name: str, lat: float, lng: float, top_k: int, requested_fields: List[str]
    ) -> List[BaseModel]:
        pass
