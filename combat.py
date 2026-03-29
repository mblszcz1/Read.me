import random
# zad 2 - osoba 1 
def attack(attacker, defender):
    damage = attacker["attack"]
    defender["hp"] -= damage

    critChance =  random.randint(0, 6)

    if critChance == 0:
        print(attacker["name"], "hits CRITICILY", defender["name"], "for", damage*4)
    elif critChance%2 == 0:
        print(attacker["name"], "hits criticly", defender["name"], "for", damage * 2)
    else:
        print(attacker["name"], "hits", defender["name"], "for", damage)

# zad 2 - osoba 3  - zmieniona wersja 

import random

def attack(attacker, defender):
    
    baseDamage = attacker["attack"]
    randomBonus = random.randint(0, 5)
    damage = baseDamage + randomBonus

    critChance = random.randint(0, 6)

    if critChance == 0:
        finalDamage = damage * 4
        print(attacker["name"], "hits CRITICLY", defender["name"], "for", finalDamage)
    elif critChance % 2 == 0:
        finalDamage = damage * 2
        print(attacker["name"], "hits criticly", defender["name"], "for", finalDamage)
    else:
        finalDamage = damage
        print(attacker["name"], "hits", defender["name"], "for", finalDamage)

    defender["hp"] -= finalDamage
