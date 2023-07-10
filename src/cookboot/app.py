import falcon.asgi
from cookboot.adapters.http.recipe import RecipeResource
from cookboot.application.recipe_book import RecipeBook


# Having this as a function simplifies testing
def create_app(recipe_book: RecipeBook) -> falcon.asgi.App:
    app = falcon.asgi.App()
    recipes = RecipeResource(recipe_book)
    app.add_route("/recipes", recipes)
    app.add_route("/recipes/{recipe_id}", recipes, suffix="recipe")

    return app
