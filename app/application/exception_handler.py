import strawberry.exceptions
import functools
from typing import Callable, Any
from pydantic import ValidationError


def handle_exceptions(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            # Pydantic ValidationError 처리
            errors = e.errors()
            detailed_errors = [
                f"Field '{error['loc'][0]}': {error['msg']}" for error in errors
            ]
            message = " | ".join(detailed_errors)
            raise strawberry.exceptions.GraphQLError(f"Validation error: {message}")
        except ValueError as e:
            # 일반적인 값 오류 처리
            raise strawberry.exceptions.GraphQLError(f"Invalid input: {e}")
        except Exception as e:
            # 모든 기타 예외 처리
            raise strawberry.exceptions.GraphQLError(f"Unexpected error: {e}")

    return wrapper
