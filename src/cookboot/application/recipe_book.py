from typing import Protocol
from cookboot.domain.recipe import Recipe


class RecipeBook(Protocol):
    def add_new_recipe(self, name: str, ingridients: list[str]) -> Recipe:
        ...
