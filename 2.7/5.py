from collections import defaultdict

class Fitness:
    def __init__(self, client_code, year, month, exercise_length):
        self._client_code = client_code
        self._year = year
        self._month = month
        self._exercise_length = exercise_length

first_exercise = Fitness(231, 2023, 3, 3.5)
second_exercise = Fitness(422, 2025, 11, 0.5)
third_exercise = Fitness(322, 2024, 5, 2.5)
fourth_exercise = Fitness(101, 2023, 6, 2)
fifth_exercise = Fitness(355, 2024, 9, 1)
sixth_exercise = Fitness(178, 2023, 4, 1.5)
seventh_exercise = Fitness(299, 2024, 7, 3.0)
eighth_exercise = Fitness(467, 2025, 12, 2.0)
ninth_exercise = Fitness(512, 2026, 2, 1.0)
tenth_exercise = Fitness(145, 2023, 8, 0.75)

exercises = [first_exercise, second_exercise, third_exercise, fourth_exercise, fifth_exercise,
             sixth_exercise, seventh_exercise, eighth_exercise, ninth_exercise, tenth_exercise]

year_table = defaultdict(int)

for exercise in exercises:
    year_table[exercise._year] += exercise._exercise_length

for key, value in year_table.items():
    if value == max(year_table.values()):
        print(key, value)