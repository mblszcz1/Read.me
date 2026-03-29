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
        tasks.show_all(lista_zadan)
    elif choice == "2":
        nowe_zadanie = input("Tresc zadania: ")
        tasks.add_task(lista_zadan, nowe_zadanie)
    elif choice == "3":
        idx = int(input("Numer zadania do usuniecia: "))
        tasks.remove_task(lista_zadan, idx)
    elif choice == "4":
        tasks.filter_tasks(lista_zadan, True)
    elif choice == "5":
        tasks.filter_tasks(lista_zadan, False)
    elif choice == "6":
        # --- TWOJA GŁÓWNA ROLA (Osoba 2) ---
        storage.save_tasks(lista_zadan)
        print("Dane zapisane. Do widzenia!")
        break
    else:
        print("Wprowadz poprawna opcje!")
        
if __name__ == "__main__":
    main()
    