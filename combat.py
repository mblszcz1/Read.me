import random

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