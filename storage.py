import json

# zad 2 - osoba 3
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
      
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
