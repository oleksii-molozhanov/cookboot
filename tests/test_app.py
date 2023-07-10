import pytest
import falcon.testing
import falcon as fl
from typing import Type, no_type_check
from cookboot.app import create_app


@pytest.fixture
def client() -> falcon.testing.TestClient:
    app = create_app()
    return falcon.testing.TestClient(app)


@no_type_check  # Disable mypy since VC Code still can't properly invoke it acknowledging --excludes
def test_recipe_get_should_succeed(client):
    # given when
    resp = client.simulate_get("/recipes")

    # then
    assert resp.status_code == 200
    assert resp.headers["content-type"] == fl.MEDIA_TEXT
    assert resp.text == "List of all recipes"


@no_type_check
def test_recipe_get_recipe_id_should_succeed(client):
    # given
    recipe_id = "avocado_yummy"

    # when
    resp = client.simulate_get(f"/recipes/{recipe_id}")

    # then
    assert resp.status_code == 200
    assert resp.headers["content-type"] == fl.MEDIA_TEXT
    assert resp.text == f"Tasty stuff: {recipe_id}"


@no_type_check
def test_app_get_unknown_route_should_fail(client):
    # given when
    resp = client.simulate_get("/non_existing_route")

    # then
    assert resp.status_code == 404
