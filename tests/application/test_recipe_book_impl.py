from typing import Tuple, no_type_check
import pytest
from cookboot.application.recipe_book_impl import RecipeBookImpl
from cookboot.application.recipe_book import RecipeBook
from cookboot.application.recipe_repo import RecipeRepo
from cookboot.adapters.persistance.recipe_repo_in_memory import RecipeRepoInMemory
from cookboot.domain.user import UserId
from cookboot.domain.recipe import Ingridient


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


@pytest.fixture
def book(repo: RecipeRepo) -> RecipeBook:
    return RecipeBookImpl(repo)


@no_type_check
def test_assignment(repo) -> None:
    assert issubclass(RecipeBookImpl, RecipeBook)
    assert isinstance(RecipeBookImpl(repo), RecipeBook)


@no_type_check
def test_add_new_recipe_fills_the_data(book: RecipeBook, ingridients, user_id, name) -> None:
    # given when
    recipe = book.add_new_recipe(name, ingridients, user_id)

    # then
    assert recipe.name == name
    assert recipe.ingridients == ingridients
    assert recipe.user_id == user_id
    assert recipe.user_id != None
