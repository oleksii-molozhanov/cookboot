import falcon as fl
import json
from cookboot.application.recipe_book import RecipeBook


class RecipeResource:
    def __init__(self, recipe_book: RecipeBook) -> None:
        self._recipe_book = recipe_book

    async def on_get(self, req: fl.Request, resp: fl.Response) -> None:
        """Handles GET requests"""
        resp.status = fl.HTTP_200  # This is the default status
        resp.content_type = fl.MEDIA_TEXT  # Default is JSON, so override
        resp.text = "List of all recipes"

    async def on_get_recipe(self, req: fl.Request, resp: fl.Response, recipe_id: str) -> None:
        """Handles GET requests"""
        resp.status = fl.HTTP_200  # This is the default status
        resp.content_type = fl.MEDIA_TEXT  # Default is JSON, so override
        resp.text = f"Tasty stuff: {recipe_id}"

    async def on_post(self, req: fl.Request, resp: fl.Response) -> None:
        data = json.loads(await req.stream.readall())

        resp.status = fl.HTTP_200
