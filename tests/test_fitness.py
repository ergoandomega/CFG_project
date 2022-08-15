import unittest
from fitness import Fitness


class TestFitness(unittest.TestCase):

    def test_get_exercise_data(self):
        exercise_data = Fitness.get_exercise_data()
        print(exercise_data)
        # Assert that there is at least one exercise
        self.assertGreater(len(exercise_data), 0)
        # Assert that Barbell Lunges is one of the exercises
        try:
            next(filter(lambda exercise: exercise['name'] == 'Barbell Lunges', exercise_data))
        except StopIteration:
            self.fail('Example exercise Barbell Lunges not present')

    def test_get_exercise_category_data(self):
        exercise_category_data = Fitness.get_exercise_category_data(14)
        # Assert that category 14 is Calves
        self.assertEqual(exercise_category_data['name'], 'Calves')


if __name__ == '__main__':
    unittest.main()
