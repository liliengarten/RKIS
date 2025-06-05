class Task:
    def __init__(self, date_start, date_finish, description):
        self._date_start = date_start
        self._date_finish = date_finish
        self._description = description

first_task = Task('01.01.2025', '02.01.2025','Поспать')
second_task = Task('01.02.2025', '02.02.2025','Сходить на рыбалку')
third_task = Task('01.03.2025', '02.03.2025','Поздравить друга ')
fourth_task = Task('01.04.2025', '02.04.2025','Сдать экзамен ')
fifth_task = Task('01.05.2025', '02.05.2025','Отпраздновать')

tasks = [first_task, second_task, third_task, fourth_task, fifth_task]

latest_task = tasks[0]

for task in tasks:
    current_task = task._date_finish.split('.')
    latest_task_info = latest_task._date_finish.split('.')

    if int(current_task[2]) > int(latest_task_info[2]):
        latest_task = task

    elif int(current_task[1]) > int(latest_task_info[1]):
        latest_task = task

    elif int(current_task[0]) > int(latest_task_info[0]):
        latest_task = task

print(latest_task._date_start, latest_task._date_finish, latest_task._description)