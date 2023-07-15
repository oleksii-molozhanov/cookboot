from typing import Union, runtime_checkable
from typing import Protocol
from cookboot.domain.recipe import Ingridient, Recipe, RecipeId
from cookboot.domain.user import UserId


@runtime_checkable
class RecipeBook(Protocol):
    def add_new_recipe(self, name: str, ingridients: list[Ingridient], user: UserId) -> Recipe:
        ...

    def get_recipe(self, id: RecipeId, user: UserId) -> Union[Recipe, None]:
        ...

    def list_all(self, user: UserId) -> list[Recipe]:
        ...
