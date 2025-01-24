import strawberry
from typing import Optional


@strawberry.input
class UpdateUserConfigInput:
    font_size: Optional[int]
