import requests
import random
import config


class Recipes:

    @staticmethod
    def get_recipes_for_ingredient(ingredient):
        try:
            recipe_data = Recipes.get_recipe_data_for_ingredient(ingredient)
            random_recipe_data = random.sample(recipe_data, k=2)
            return [recipe_data['recipe'] for recipe_data in random_recipe_data]
        except (requests.exceptions.RequestException, ValueError):
            return []

    @staticmethod
    def get_recipe_data_for_ingredient(ingredient):
        response = requests.get(
            f"https://api.edamam.com/api/recipes/v2?type=public"
            f"&q={ingredient}"
            f"&app_id={config.edamam_app_id}"
            f"&app_key={config.edamam_app_key}"
            f"&diet=low-fat"
            f"&dishType=Main%20course")
        return response.json()['hits']
