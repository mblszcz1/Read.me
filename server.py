def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    users = []
    passwords = []

    for i in users:
        if name == users[i] and password == passwords[i]:
            print("Login successful")
            return True
        elif name == users[i] and password != passwords[i]:
            print("Wrong password. Try again")
            return False
        elif name != users[i] and password == passwords[i]:
            continue

    return False