import unittest
import profile


class TestProfile(unittest.TestCase):

    def test_calculate_bmi(self):
        test_height = 170
        test_weight = 65
        bmi = profile.calculate_bmi(test_height, test_weight)
        self.assertEqual(bmi, 22)

    def test_get_fitness_goal(self):
        test_bmi_underweight = 15
        test_bmi_ideal_weight = 22
        test_bmi_overweight = 28
        self.assertEqual(profile.get_fitness_goal(test_bmi_underweight), "Gain weight")
        self.assertEqual(profile.get_fitness_goal(test_bmi_ideal_weight), "Maintain weight")
        self.assertEqual(profile.get_fitness_goal(test_bmi_overweight), "Lose weight")


if __name__ == '__main__':
    unittest.main()
