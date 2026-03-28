from combat import attack
from characters import player, enemy

def main():
    while player["hp"] > 0 and enemy["hp"] > 0:
        attack(player, enemy)
        attack(enemy, player)

    if player["hp"] <= 0:
        print("You lost!")
    else:
        print("You won!")

def task_menu():
    print("!oto listan zadan! \n 1) pokaz zadania \n 2) dodaj zadania \n 3) usun zadania 4) pokaz zadania zrobione \n 5) pokaz zadania nie zrobione \n 6) zapisz i wyjdz \n")

    choice = input("\nCo chcesz zrobic? ")

    if choice == "1":
        print("Pokaz zadania!")
    elif choice == "2":
        print("Dodaj zadania!")
    elif choice == "3":
        print("USUN zadania!")
    elif choice == "4":
        print("Pokaz zadania zrobione!")
    elif choice == "5":
        print("Pokaz zadania niezrobione!")
    elif choice == "6":
        print("Zapisz i wyjdz!")
    else:
        print("wprowaddz poprawna opcje")

if __name__ == "__main__":
    main()