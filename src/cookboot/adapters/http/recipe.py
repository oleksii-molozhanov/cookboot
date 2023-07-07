import falcon as fl
from typing import Callable
import json


class RecipeResource:
    async def on_get(self, req: fl.Request, resp: fl.Response) -> Callable:
        """Handles GET requests"""
        resp.status = fl.HTTP_200  # This is the default status
        resp.content_type = fl.MEDIA_TEXT  # Default is JSON, so override
        resp.text = "List of all recipes"

    async def on_get_recipe(self, req: fl.Request, resp: fl.Response, recipe_id: str) -> Callable:
        """Handles GET requests"""
        resp.status = fl.HTTP_200  # This is the default status
        resp.content_type = fl.MEDIA_TEXT  # Default is JSON, so override
        resp.text = f"Tasty stuff: {recipe_id}"

    async def on_post(self, req: fl.Request, resp: fl.Response) -> Callable:
        data = json.loads(await req.stream.readall())
        resp.status = fl.HTTP_200
