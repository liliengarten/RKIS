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

exercises = [first_exercise, second_exercise, third_exercise, fourth_exercise, fifth_exercise]

shortest_exercise = exercises[0]
longest_exercise = exercises[0]

for exercise in exercises:
    if exercise._exercise_length < shortest_exercise._exercise_length:
        shortest_exercise = exercise

    elif exercise._exercise_length > longest_exercise._exercise_length:
        longest_exercise = exercise

print(shortest_exercise._client_code, shortest_exercise._year, shortest_exercise._month, shortest_exercise._exercise_length)
print(longest_exercise._client_code, longest_exercise._year, longest_exercise._month, longest_exercise._exercise_length)
