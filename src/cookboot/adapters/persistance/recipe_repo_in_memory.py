from cookboot.domain.recipe import Ingridient, Recipe, RecipeId
from cookboot.domain.user import UserId
from uuid import uuid4


class RecipeRepoInMemory:
    """In memory implementation of RecipeRepo protocol.
    Usefull for testing."""

    def __init__(self) -> None:
        self._repo: dict[RecipeId, Recipe] = dict()

    def create(self, name: str, ingridients: list[Ingridient], user_id: UserId) -> Recipe:
        id: RecipeId = str(uuid4())
        recipe = Recipe(id, name, ingridients, user_id)
        self._repo[id] = recipe

        return recipe

    def get(self, id: RecipeId, user_id: UserId) -> Recipe:
        try:
            recipe = self._repo[id]
        except KeyError:
            return None

        if recipe.user_id != user_id:
            return None

        return recipe
