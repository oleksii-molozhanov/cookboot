import imp
from typing import Protocol, runtime_checkable
from cookboot.domain.recipe import Ingridient, Recipe, RecipeId
from cookboot.domain.user import UserId


@runtime_checkable
class RecipeRepo(Protocol):
    """Interface for Recipe repository.
    Note: recipes are owned by users.
    Note: there is no guarantee of uniqueness of recipe_id between several users."""

    def get(self, id: RecipeId, user_id: UserId) -> Recipe:
        ...

    def create(self, name: str, ingridients: list[Ingridient], user_id: UserId) -> Recipe:
        ...
