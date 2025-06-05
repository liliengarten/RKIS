line = 'zaaaz azaz zaza zacvbz'
symbol = 'z'

for combination in line.split():
    if len(combination) > 1 and combination[0] == symbol and combination[len(combination) - 1] == symbol:
        print(combination)