from uuid import UUID, uuid4
from cookboot.domain.recipe import Recipe
from typing import Type


class RecipeBook:
    def __init__(self) -> None:
        # this will be used for now instead of a direct query to repo
        self._recipes: dict[UUID, Type[Recipe]] = {}

    def add_new_recipe(self, name: str, ingridients: list[str]) -> Recipe:
        id = uuid4()  # Later this will be provided by the repo
        recipe = Recipe(id, name, ingridients)
        self._recipes[id] = recipe
        return recipe
