# zad 2 - funkcje pomocnicze

def get_user_input():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    return name, password


def get_users():
    return ["Przemek", "bartek", "Michał"]


def get_passwords():
    return ["1234", "abcd", "pass"]


def find_user_index(name, users):
    for i in range(len(users)):
        if users[i] == name:
            return i
    return -1


def check_password(index, password, passwords):
    if index == -1:
        return False
    return passwords[index] == password


def show_login_success():
    print("Login successful")


def show_wrong_password():
    print("Wrong password. Try again")


def show_user_not_found():
    print("User not found")
