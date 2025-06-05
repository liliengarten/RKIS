import random

numbers = []

while len(numbers) < 10:
    random_number = random.randint(-10, 10)
    numbers.append(random_number)

positive_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)

print(numbers)
print(positive_numbers)