import falcon.asgi

from adapters.http.recipe import RecipeResource

app = application = falcon.asgi.App()
app.add_route("/recipes", RecipeResource())
