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
