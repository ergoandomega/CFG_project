import requests
import random

exercise_endpoint = "https://wger.de/api/v2/exercise/"
exercise_category_endpoint = "https://wger.de/api/v2/exercisecategory/"

# English (German is language 1)
params = {
    'language': 2
}


class Fitness:

    @staticmethod
    def get_random_exercises():
        random_exercise_data = random.sample(Fitness.get_exercise_data(), k=3)
        random_exercises_to_return = []
        for random_exercise in random_exercise_data:
            exercise_category_data = Fitness.get_exercise_category_data(random_exercise['category'])
            random_exercises_to_return.append({'name': random_exercise['name'], 'category': exercise_category_data['name']})
        return random_exercises_to_return

    @staticmethod
    def get_exercise_data():
        exercise_response = requests.get(url=exercise_endpoint, params=params)
        exercise_data = exercise_response.json()
        return exercise_data['results']

    @staticmethod
    def get_exercise_category_data(category):
        exercise_category_response = requests.get(url=exercise_category_endpoint + str(category),
                                                  params=params)
        exercise_category_data = exercise_category_response.json()
        return exercise_category_data
