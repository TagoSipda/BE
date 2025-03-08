from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import List, Optional


class GetBusStopValidator(BaseModel):
    id: int = Field(..., ge=1, description="ID must be greater than or equal to 1.")
    requested_field: List[str] = Field(
        ...,
        min_items=1,
        description="Requested fields must contain at least one field.",
    )


class SearchBusStopsValidator(BaseModel):
    name: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    top_k: int = Field(
        ..., ge=1, description="Top K must be greater than or equal to 1."
    )
    requested_fields: List[str] = Field(
        ...,
        min_items=1,
        description="Requested fields must contain at least one field.",
    )

    @model_validator(mode="after")
    def check_lat_lng(self) -> "SearchBusStopsValidator":
        lat, lng = self.lat, self.lng
        if (lat is None and lng is not None) or (lat is not None and lng is None):
            raise ValueError("Both lat and lng must be provided together.")
        return self
