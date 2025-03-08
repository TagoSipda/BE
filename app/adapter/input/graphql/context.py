from fastapi import Depends, Request
from strawberry.fastapi import BaseContext

from app.application.use_cases.bus_stop import BusStopUseCase
from app.config.dependencies import get_bus_stop_use_case


class GraphQLContext(BaseContext):
    def __init__(
        self,
        request: Request,
        bus_stop_use_case: BusStopUseCase = Depends(get_bus_stop_use_case),
    ):
        super().__init__()
        self.request = request
        self.bus_stop_use_case = bus_stop_use_case


async def get_context(
    request: Request, bus_stop_use_case: BusStopUseCase = Depends(get_bus_stop_use_case)
) -> GraphQLContext:
    return GraphQLContext(request=request, bus_stop_use_case=bus_stop_use_case)
