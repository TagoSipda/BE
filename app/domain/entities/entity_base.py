from pydantic import BaseModel, create_model


class Entity(BaseModel):
    """도메인 Entity의 베이스 클래스입니다.

    불변성을 보장하며(frozen), GraphQL 쿼리에 맞춰 동적 Projection을 생성하는 기능을 제공합니다."""

    model_config = {"frozen": True}  # 인스턴스 생성 후 필드 수정 불가 (불변성 보장)

    @classmethod
    def create_projection(cls, data: dict, requested_fields: list[str]) -> BaseModel:
        """requested_fields에 해당하는 필드만 포함하는 동적 Projection 모델을 생성합니다.

        GraphQL에서 요청된 필드만 선택적으로 조회하여 불필요한 데이터 로드를 방지합니다."""

        # 1. requested_fields에 해당하는 필드 타입 추출
        projection_fields = {
            name: (cls.model_fields[name].annotation, cls.model_fields[name].default)
            for name in requested_fields
            if name in cls.model_fields
        }

        # 2. 동적 Pydantic 모델 생성
        ProjectionClass = create_model(f"{cls.__name__}Projection", **projection_fields)

        # 3. 데이터로 인스턴스 생성
        filtered_data = {k: v for k, v in data.items() if k in requested_fields}
        return ProjectionClass(**filtered_data)
