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


# Baza danych użytkowników (zgodnie z rolą Bartka w 'storage')
users_db = {"admin": "1234", "bartek": "pancerz123"}
messages = []  # Tu będą trafiać wiadomości (w utils.py lub server.py)


def login():
    print("--- LOGIN SYSTEM ---")
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    if name in users_db and users_db[name] == password:
        print(f"Welcome, {name}!")
        return name  # Zwracamy nick, żeby wiedzieć kto wysyła wiadomości
    else:
        print("Access denied.")
        return None


def start_chat(username):
    print(f"\n--- Chat Room (User: {username}) ---")
    print("Type your message or '/exit' to quit.")

    while True:
        msg_text = input(f"{username}> ")

        if msg_text == "/exit":  # Komenda z README
            print("Exiting chat...")
            break

        # Tworzymy strukturę wiadomości
        message_entry = f"[{username}]: {msg_text}"
        messages.append(message_entry)

        # Symulacja wyświetlania chatu
        print("\n--- RECENT MESSAGES ---")
        for m in messages[-5:]:  # Pokazuje 5 ostatnich wiadomości
            print(m)
        print("-----------------------\n")


# --- URUCHOMIENIE ---
user = login()
if user:
    start_chat(user)