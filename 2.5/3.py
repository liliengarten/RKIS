import random

def get_arr():
    arr = []

    for i in range(10):
        random_number = random.randint(1, 100)

        if random_number % 2 == 0:
            arr.append(random_number)

    return sorted(arr)