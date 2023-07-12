from dataclasses import dataclass
from typing import NewType

from cookboot.domain.user import UserId


Ingridient = NewType("Ingridient", str)
RecipeId = NewType("RecipeId", str)


@dataclass
class Recipe:
    id: RecipeId
    name: str
    ingridients: list[Ingridient]
    user_id: UserId
