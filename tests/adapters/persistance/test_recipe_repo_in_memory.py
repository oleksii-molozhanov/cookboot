from cookboot.application.recipe_repo import RecipeRepo
from cookboot.adapters.persistance.recipe_repo_in_memory import RecipeRepoInMemory
from cookboot.domain.recipe import Ingridient
from cookboot.domain.user import UserId
from typing import Tuple, no_type_check
import pytest


@pytest.fixture
def ingridients() -> Tuple[Ingridient, ...]:
    return (Ingridient("avocado"), Ingridient("love"))


@pytest.fixture
def user_id() -> UserId:
    return "user_007"


@pytest.fixture
def name() -> str:
    return "yummy avocado"


@pytest.fixture
def repo() -> RecipeRepo:
    return RecipeRepoInMemory()


@no_type_check
def test_created_recipe_fills_the_data(repo: RecipeRepo, ingridients, user_id, name) -> None:
    # given when
    recipe = repo.create(name, ingridients, user_id)

    # then
    assert recipe.name == name
    assert recipe.ingridients == ingridients
    assert recipe.user_id == user_id
    assert recipe.user_id != None


@no_type_check
def test_get_existing_recipe_returns_the_data(repo: RecipeRepo, ingridients, user_id) -> None:
    # given when
    recipe = repo.create(name, ingridients, user_id)
    gotten = repo.get(recipe.id, user_id)

    # then
    assert recipe == gotten


@no_type_check
def test_get_existing_recipe_wrong_user_returns_none(repo: RecipeRepo, ingridients, user_id) -> None:
    # given
    wrong_user_id = "user_wrong"

    # when
    recipe = repo.create(name, ingridients, user_id)
    gotten = repo.get(recipe.id, wrong_user_id)

    # then
    assert gotten == None


@no_type_check
def test_get_non_existing_recipe_returns_none(repo: RecipeRepo, user_id) -> None:
    # given when
    recipe = repo.get("non-existing-id", user_id)

    # then
    assert recipe == None


@no_type_check
def test_same_name_recipe_can_be_created(repo: RecipeRepo, ingridients, user_id) -> None:
    # given when
    recipe1 = repo.create(name, ingridients, user_id)
    recipe2 = repo.create(name, ingridients, user_id)

    # then
    assert recipe1 != recipe2


def test_assignment() -> None:
    assert issubclass(RecipeRepoInMemory, RecipeRepo)
    assert isinstance(RecipeRepoInMemory(), RecipeRepo)
