from shutil import ExecError
import pytest
import falcon.testing
import falcon as fl
from cookboot.app import create_app


@pytest.fixture
def client():
    app = create_app()
    return falcon.testing.TestClient(app)


def test_recipe_get_should_succeed(client):
    # given when
    resp = client.simulate_get("/recipes")

    # then
    assert resp.status_code == 200
    assert resp.headers["content-type"] == fl.MEDIA_TEXT
    assert resp.text == "List of all recipes"


def test_recipe_get_recipe_id_should_succeed(client):
    # given
    recipe_id = "avocado_yummy"

    # when
    resp = client.simulate_get(f"/recipes/{recipe_id}")

    # then
    assert resp.status_code == 200
    assert resp.headers["content-type"] == fl.MEDIA_TEXT
    assert resp.text == f"Tasty stuff: {recipe_id}"
