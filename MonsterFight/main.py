from character import Character as ch
import time

playerName = input("Enter Player Name: ")
playerHealth = int(input("Enter Player Health: "))
EnemyName = input("Enter Enemy Name: ")
EnemyHealth = int(input("Enter Enemy Health: "))
player = ch(playerName, playerHealth)
enemy = ch(EnemyName, EnemyHealth)


time.sleep(2)
print(f"Welcome to Battel Field {playerName}, Your enemy is {EnemyName}")
time.sleep(3)
print(
    f"This Battel will heald Until anyone die or scape. \nHealth 0 means die \n{playerName} you can skip the battle any time"
)
time.sleep(3)
print(f"You punch the Monster 1st then the Monster will gives you back punch.")
time.sleep(3)

print(f"Let's start the fight {playerName}")
time.sleep(5)

while True:
    choice = int(input("0. Punch the Enemy\n1. Escape the battle filed\n"))
    if choice == 0:
        # player chanches
        damage = enemy.give_damage()
        print(f"{playerName} you gave {EnemyName}, {damage} damage")
        print(f"{EnemyName}'s health is {enemy.gethealth()}\n")

        time.sleep(2)

        # enemy chances
        damage = player.give_damage()
        print(f"{EnemyName} gaves you {playerName}, {damage} damage")
        print(f"{playerName}'s health is {player.gethealth()}\n")
        if not player.is_alive():
            print(f"{playerName} you lose. {EnemyName} win")
            break
        if not enemy.is_alive():
            print(f"{playerName} Hoooray! You loose the {EnemyName}")
            break
    elif choice == 1:
        print(f"Shame {playerName}, you escape the fight, The Monster Win.")
        break
    else:
        print(f"Wrong Choose, Please try with 1 or 0")
        continue
