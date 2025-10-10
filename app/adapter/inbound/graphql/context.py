from typing import List
from fastapi import Depends, Request
from strawberry.fastapi import BaseContext
from strawberry.dataloader import DataLoader

from app.application.use_case.bus_stop import BusStopUseCaseImpl
from app.application.use_case.bus_route import BusRouteUseCaseImpl
from app.application.interfaces.inbound.graphql.dto import (
    BusStopOutputDTO,
    BusRouteOutputDTO,
)


class GraphQLContext(BaseContext):
    def __init__(
        self,
        request: Request,
        bus_stop_use_case: BusStopUseCaseImpl,
        bus_route_use_case: BusRouteUseCaseImpl,
    ):
        super().__init__()
        self.request = request
        self.bus_stop_use_case = bus_stop_use_case
        self.bus_route_use_case = bus_route_use_case

        # DataLoader 초기화
        self.bus_stop_loader = DataLoader(load_fn=self._load_bus_stops)
        self.bus_route_loader = DataLoader(load_fn=self._load_bus_routes)

    async def _load_bus_stops(self, keys: List[int]) -> List[BusStopOutputDTO]:
        """여러 BusStop ID를 한 번에 조회 - DataLoader용"""
        # 중복 제거하고 조회
        bus_stops = await self.bus_stop_use_case.get_bus_stops_by_ids(list(set(keys)))

        # key 순서대로 매핑 (DataLoader는 요청 순서대로 반환해야 함)
        bus_stop_map = {stop.id: stop for stop in bus_stops}
        return [bus_stop_map.get(key) for key in keys]

    async def _load_bus_routes(self, keys: List[int]) -> List[BusRouteOutputDTO]:
        """여러 BusRoute ID를 한 번에 조회 - DataLoader용"""
        # 중복 제거하고 조회
        bus_routes = await self.bus_route_use_case.get_bus_routes_by_ids(
            list(set(keys))
        )

        # key 순서대로 매핑
        bus_route_map = {route.id: route for route in bus_routes}
        return [bus_route_map.get(key) for key in keys]


async def get_context(
    request: Request,
    bus_stop_use_case: BusStopUseCaseImpl,
    bus_route_use_case: BusRouteUseCaseImpl,
) -> GraphQLContext:
    """GraphQL Context 생성 - 의존성 주입"""
    return GraphQLContext(
        request=request,
        bus_stop_use_case=bus_stop_use_case,
        bus_route_use_case=bus_route_use_case,
    )
