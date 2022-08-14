def calculate_bmi(height, weight):
    return round(weight / ((height / 100) ** 2))


def get_fitness_goal(bmi):
    if bmi <= 18.5:
        return "Gain weight"
    elif bmi <= 25:
        return "Maintain weight"
    else:
        return "Lose weight"
