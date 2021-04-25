from time import sleep
from sprite import Sprite

#validation of input data
def verification():
    name = input("Enter character name: ")
    try:
        health = int(input(f"Enter {name}'s health level: "))
        attack = int(input(f"Enter {name}'s damage level: "))
    except ValueError:
        print('Please enter numbers, not strings')
        return verification()
    return name, health, attack

#creation of 2 characters
name, health, attack = verification()
player = Sprite(name, health, attack)

name, health, attack = verification()
computer = Sprite(name, health, attack)

player.print_info(computer)

#main
if input('Start the battle? \n YES \n NO \n -->> ').lower() == 'yes':
    print('\n LET THE BATTLE BEGIN! \n')
    sleep(4)
    player.fight(computer)
    sleep(4)
    if computer.health > 0 and computer.health < 35:
        computer.chance_heal = 0.31
        print('\n' + f"{computer.name}'s health has reached a critically low level. So he increased the likelihood of healing \n")
else:
    print("The game did not take place")
