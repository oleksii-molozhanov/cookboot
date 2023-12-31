from typing import Tuple, no_type_check
import pytest
from cookboot.domain.recipe import Recipe, Ingridient


@pytest.fixture
def ingridients() -> Tuple[Ingridient, ...]:
    return (Ingridient("avocado"), Ingridient("love"))


@no_type_check  # Disable mypy since VC Code still can't properly invoke it acknowledging --excludes
def test_create_recipe_with_initializer_should_set_parameters(ingridients) -> None:
    # given
    name = "Fried avocado"
    id = "random_id"

    # when
    recipe = Recipe(id, name, ingridients=ingridients)

    # then
    assert recipe.id == id
    assert recipe.name == name
    assert recipe.ingridients == ingridients


@no_type_check
def test_create_recipe_without_id_should_fail(ingridients) -> None:
    # given
    name = "Fried avocado"

    # when then
    with pytest.raises(TypeError):
        Recipe(name, ingridients)
