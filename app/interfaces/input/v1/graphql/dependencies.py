from fastapi import Depends
from strawberry.fastapi import BaseContext

from app.application.use_cases.bus_stop import BusStopUseCase
from app.application.services.bus_stop import BusStopService


class CustomContext(BaseContext):
    def __init__(self, bus_stop_use_case: BusStopUseCase):
        self.bus_stop_use_case = bus_stop_use_case


def get_bus_stop_use_case() -> BusStopUseCase:
    return BusStopService()


async def get_context(
    bus_stop_use_case: BusStopUseCase = Depends(get_bus_stop_use_case),
) -> CustomContext:
    return CustomContext(bus_stop_use_case=bus_stop_use_case)
