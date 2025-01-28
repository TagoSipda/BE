from typing import List, Optional
from pydantic import BaseModel


class GetBusStopRequestDTO(BaseModel):
    id: int
    requested_field: List[str]


class SearchBusStopsRequestDTO(BaseModel):
    name: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    top_k: int
    requested_fields: List[str]
