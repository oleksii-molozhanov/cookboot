import falcon.asgi
from adapters.http.recipe import RecipeResource


# Having this as a function simplifies testing
def create_app() -> falcon.asgi.App:
    app = falcon.asgi.App()
    recipes = RecipeResource()
    app.add_route("/recipes", recipes)
    app.add_route("/recipes/{recipe_id}", recipes, suffix="recipe")

    return app
