import random

numbers = []

while len(numbers) < 10:
    random_number = random.randint(-10, 10)
    numbers.append(random_number)

first_positive = 0
last_negative = 0

for number in numbers:
    if number > 0:
        first_positive = number
        break

for number in numbers[::-1]:
    if number < 0:
        last_negative = number
        break

print(first_positive, last_negative)