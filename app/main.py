from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from contextlib import asynccontextmanager
import asyncio

from app.interfaces.input.v1.graphql.schema import schema


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 앱이 시작될 때 실행할 코드
    print("앱이 시작됩니다.")
    # 초기화 로직 (예: DB 연결)

    yield  # 여기가 실제로 앱이 동작하는 시점입니다.

    # 앱이 종료될 때 실행할 코드
    print("앱이 종료됩니다.")
    # 정리 로직 (예: DB 연결 종료)


app = FastAPI(docs_url="/docs", openapi_url="/open-api-docs", lifespan=lifespan)
app.add_route(
    "/api/v1/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler())
)
