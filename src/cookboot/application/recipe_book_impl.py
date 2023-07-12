from uuid import UUID, uuid4
from typing import Type
from cookboot.domain.recipe import Recipe
from cookboot.application.recipe_repo import RecipeRepo


class RecipeBookImpl:
    """Implementation of RecipeBook protocol."""

    def __init__(self, repo: RecipeRepo) -> None:
        # this will be used for now instead of a direct query to repo
        self._repo = repo

    def add_new_recipe(self, name: str, ingridients: list[str]) -> Recipe:
        return self._repo.create(name, ingridients)
