import falcon.asgi
from adapters.http.recipe import RecipeResource

app = falcon.asgi.App()
recipes = RecipeResource()
app.add_route("/recipes", recipes)
app.add_route("/recipes/{recipe_id}", recipes, suffix="recipe")
