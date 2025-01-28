from abc import ABC, abstractmethod
from fastapi import Depends
from typing import List

from app.dtos.request.bus_stop import GetBusStopRequestDTO
from app.dtos.request.bus_stop import SearchBusStopsRequestDTO
from app.dtos.response.bus_stop import GetBusStopResponseDTO
from app.dtos.response.bus_stop import SearchBusStopsResponseDTO


class BusStopUseCase(ABC):
    @abstractmethod
    def find_by_id(dto: GetBusStopRequestDTO) -> GetBusStopResponseDTO:
        pass

    @abstractmethod
    def search_bus_stops(dto: SearchBusStopsRequestDTO) -> SearchBusStopsResponseDTO:
        pass
