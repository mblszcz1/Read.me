from pynput.keyboard import Key, Controller
#zadanie 2 - osoba 1
def snakeMovement():
    keyboard = Controller()

    moveX = 0
    moveY = 0

    if keyboard.pressed(Key.arrowUp):
        moveX, moveY = 0, 10
    elif keyboard.pressed(Key.arrowDown):
        moveX, moveY = 0, -10
    elif keyboard.pressed(Key.arrowLeft):
        moveX, moveY = -10, 0
    elif keyboard.pressed(Key.arrowRight):
        moveX, moveY = 10, 0

    return moveX, moveY

#zadnie 3 - osoba 3

def setDifficulty(level):
    if level == "easy":
        return {
            "speed": 5,
            "pointsMultiplier": 1
        }
    elif level == "medium":
        return {
            "speed": 10,
            "pointsMultiplier": 2
        }
    elif level == "hard":
        return {
            "speed": 15,
            "pointsMultiplier": 3
        }
    else:
        return {
            "speed": 10,
            "pointsMultiplier": 2
        }

class ScoreManager:
    def __init__(self):
        self.current_score = 0

    def add_point(self, amount=10):
        self.current_score += amount

    def reset_score(self):
        self.current_score = 0

    def get_score(self):
        return self.current_score