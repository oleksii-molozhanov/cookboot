from typing import Union
from cookboot.domain.recipe import Recipe, RecipeId, Ingridient
from cookboot.domain.user import UserId
from cookboot.application.recipe_repo import RecipeRepo


class RecipeBookImpl:
    """Implementation of RecipeBook protocol."""

    def __init__(self, repo: RecipeRepo) -> None:
        self._repo = repo

    def add_new_recipe(self, name: str, ingridients: list[Ingridient], user: UserId) -> Recipe:
        """Creates a new recipe, stores it in the repo and returns it."""
        return self._repo.create(name, ingridients, user)

    def get_recipe(self, id: RecipeId, user: UserId) -> Union[Recipe, None]:
        """Returns a recipe from repo by RecipeId for the given UserId.
        Returns None if a recipe is not found."""

    def list_all(self, user: UserId) -> list[Recipe]:
        """Returns all recipes of the user."""
        return []
