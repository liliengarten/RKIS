class User:
    def __init__(self, login, password):
        self._login = login
        self._password = password

first_user = User('perviy', 123)
second_user = User('vtoroy', 456)
third_user = User('tretiy', 789)
fourth_user = User('chetvertiy', 101)
fifth_user = User('pyatiy', 102)

user_list = [first_user, second_user, third_user, fourth_user, fifth_user]

for user in user_list:
    if user._login == 'perviy' and user._password == 123:
        print(user._login, user._password)