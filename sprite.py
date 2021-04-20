from random import randint
from time import sleep

class Sprite():
    #character class constructor
    def __init__(self, name, health = 100, attack = 10):
        self.name = name #character name
        self.health = health #health level (default 100)
        self.attack = attack #damage level (default 10)

    #character status message
    def print_info(self,enemy):
        print("-"*40)
        print("Character`s name: " + self.name + "\n" + 'Health level: ' + str(self.health) + '\n') 
        print("Character`s name: " + enemy.name + "\n" + 'Health level: ' + str(enemy.health) + '\n') 
        print("-"*40)

    #one character strikes another character
    def strike(self, enemy):
        attack = randint(1, 3)
        #do moderate damage
        if attack == 1:
            damage = randint(self.attack-5, self.attack+10)
            enemy.health -= damage
            print(self.name + ' attacks ' + enemy.name + ' with the force of the blow ' + str(damage) + '\n')
        #do heavy damage
        elif attack == 2:
            damage = randint(self.attack-10, self.attack+30)
            enemy.health -= damage
            print(self.name + ' attacks ' + enemy.name + ' with the force of the blow ' + str(damage) + '\n')  
        #heal character
        else:
            heal = randint(self.attack-5, self.attack+10)
            self.health += heal
            print(self.name + ' healed and now his health is ' + str(self.health) + '\n')
            sleep(3)
        self.print_info(enemy)
        
    #duel
    def fight(self, enemy):
        while self.health and enemy.health > 0:
            rand = randint(0, 1)
            if rand:
                self.strike(enemy)
                if enemy.health <= 0:
                    print(enemy.name, 'fell in this difficult battle!\n')
                    break
                sleep(5)   
            else:
                enemy.strike(self)
                if self.health <= 0:
                   print(self.name, 'fell in this difficult battle!\n')
                   break
                sleep(5)   