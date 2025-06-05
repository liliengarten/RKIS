import random

numbers = []

while len(numbers) < 10:
    random_number = random.randint(-100, 100)
    numbers.append(random_number)

positive_numbers = []

for number in numbers:
    if number > 0 and len(str(number)) == 2:
        positive_numbers.append(number)

positive_numbers = sorted(positive_numbers)

print(numbers)
print(positive_numbers)