from ast import Call
from urllib import response
import falcon as fl
from typing import Callable


class RecipeResource:
    async def on_get(self, req: fl.Request, resp: fl.Response) -> Callable:
        """Handles GET requests"""
        resp.status = fl.HTTP_200  # This is the default status
        resp.content_type = fl.MEDIA_TEXT  # Default is JSON, so override
        resp.text = "Sweet stuff"

    async def on_get_recipe(self, req: fl.Request, resp: fl.Response, recipe_id: str):
        """Handles GET requests"""
        resp.status = fl.HTTP_200  # This is the default status
        resp.content_type = fl.MEDIA_TEXT  # Default is JSON, so override
        resp.text = f"Salty stuff: {recipe_id}"
