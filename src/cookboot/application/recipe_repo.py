import imp
from typing import Protocol
from cookboot.domain.recipe import Ingridient, Recipe
from cookboot.domain.user import UserId


class RecipeRepo(Protocol):
    """Interface for Recipe repository.
    Note: recipes are owned by users.
    Note: there is no guarantee of uniqueness of recipe_id between several users."""

    def get(self, id: str) -> Recipe:
        ...

    def create(self, name: str, ingridients: list[Ingridient], user_id: UserId) -> Recipe:
        ...
