from fastapi import Depends, Request
from app.adapter.output.repositories_impl.bus_stop import BusStopRepositoryImpl
from app.adapter.output.repositories_impl.bus_route import BusRouteRepositoryImpl
from app.application.repositories.bus_stop import BusStopRepository
from app.application.repositories.bus_route import BusRouteRepository
from app.application.use_cases.bus_stop import BusStopUseCase
from app.application.use_cases_impl.bus_stop import BusStopUseCaseImpl
from app.common.env import ENV


def get_bus_stop_repository() -> BusStopRepository:
    return BusStopRepositoryImpl(env=ENV)


def get_bus_route_repository() -> BusRouteRepository:
    return BusRouteRepositoryImpl(env=ENV)
