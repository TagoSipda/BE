from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
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

# Strawberry GraphQL Router 연결
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/api/v1/graphql")
