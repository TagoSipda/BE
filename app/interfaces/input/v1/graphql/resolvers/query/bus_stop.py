import strawberry
from typing import List, Optional
from fastapi import Depends
from strawberry.types import Info


from app.interfaces.input.v1.graphql.resolvers.type.bus_stop import BusStop
from app.interfaces.input.v1.graphql.validators.bus_stop import (
    GetBusStopValidator,
    SearchBusStopsValidator,
)
from app.application.exception_handler import handle_exceptions
from app.dtos.request.bus_stop import GetBusStopRequestDTO
from app.dtos.request.bus_stop import SearchBusStopsRequestDTO
from app.dtos.response.bus_stop import GetBusStopResponseDTO
from app.dtos.response.bus_stop import SearchBusStopsResponseDTO


@strawberry.type
class BusStopQuery:
    @strawberry.field
    @handle_exceptions
    def bus_stop(self, info: Info, id: int) -> BusStop:
        # Get context from info
        bus_stop_use_case = info.context.bus_stop_use_case
        requested_fields: List[str] = [field.name for field in info.selected_fields]

        # Detailed Validate
        validated_data: GetBusStopValidator = GetBusStopValidator(
            id=id, requested_field=requested_fields
        )

        # Request to Service
        request_dto: GetBusStopRequestDTO = GetBusStopRequestDTO(
            **validated_data.model_dump()
        )
        response: GetBusStopResponseDTO = bus_stop_use_case.find_by_id(request_dto)

        # Convert DTO to Strawberry Type
        response: BusStop = BusStop(**response.model_dump())
        return response

    @strawberry.field
    @handle_exceptions
    def search_bus_stops(
        self,
        info: Info,
        name: Optional[str] = None,
        lat: Optional[float] = None,
        lng: Optional[float] = None,
        top_k: int = 5,
    ) -> List[BusStop]:
        # Get context from info
        bus_stop_use_case = info.context.bus_stop_use_case
        requested_fields: List[str] = [
            field.name for field in info.selected_fields[0].selections
        ]

        # Detailed Validate
        validated_data: SearchBusStopsValidator = SearchBusStopsValidator(
            name=name, lat=lat, lng=lng, top_k=top_k, requested_fields=requested_fields
        )

        # Request to Service
        request_dto: SearchBusStopsRequestDTO = SearchBusStopsRequestDTO(
            **validated_data.model_dump()
        )
        response: SearchBusStopsResponseDTO = bus_stop_use_case.search_bus_stops(
            request_dto
        )

        # Convert DTO to Strawberry Type
        response: List[BusStop] = [
            BusStop(**item.model_dump()) for item in response.bus_stops
        ]

        return response
