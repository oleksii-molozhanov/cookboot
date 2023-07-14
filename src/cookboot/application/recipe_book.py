from typing import Protocol
from cookboot.domain.recipe import Ingridient, Recipe


class RecipeBook(Protocol):
    def add_new_recipe(self, name: str, ingridients: list[Ingridient]) -> Recipe:
        ...
