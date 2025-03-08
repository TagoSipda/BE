import sys

from dataclasses import dataclass, fields
from typing import Optional, get_type_hints, get_origin, Type, Any


def create_entity_projection(entity_class: Type) -> None:
    # 타입 힌트 가져오기
    hints = get_type_hints(entity_class)

    # 새로운 클래스의 어노테이션 생성
    annotations = {}

    for f in fields(entity_class):
        type_hint = hints.get(f.name)

        # 이미 Optional인 경우 그대로 유지, 아니면 Optional로 변환
        if get_origin(type_hint) is Optional:
            optional_type = type_hint
        else:
            optional_type = Optional[type_hint]

        annotations[f.name] = optional_type

    # 클래스 이름 생성
    dto_name = f"{entity_class.__name__}Projection"

    # 클래스 네임스페이스 생성
    namespace = {
        "__annotations__": annotations,
    }

    # 모든 필드에 기본값 None 설정
    for f_name in annotations:
        namespace[f_name] = None

    # 새로운 클래스 동적 생성
    EntityDTO = type(dto_name, (), namespace)

    # dataclass 데코레이터 적용
    EntityDTO = dataclass(EntityDTO)

    # 모듈에 클래스 등록
    module = sys.modules[entity_class.__module__]
    setattr(module, dto_name, EntityDTO)


def projection_factory(cls):
    """
    Entity 클래스에 대한 Projection 클래스를 생성하는 데코레이터
    """
    # Projection 클래스 생성 및 모듈 등록 (부분적 Fetching에 따른 전체 attribute optional화)
    _ = create_entity_projection(cls)

    # 원본 클래스 반환
    return cls
