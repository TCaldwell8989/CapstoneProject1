#############
# Main game #
##############################
# Designed By Tyler Caldwell #
##############################

from enemies import *
from player import *
from heroes import *

import sys
import random

# Dictionary containing the actions a user can do on their turn
actions = { 1 : 'search', 2 : 'camp', 3 : 'stats', 4 : 'help', 5 : 'exit'}
# Instantiate a player object with default values
player = Player("Default", 1, 1, 1)

# Start of the Command Line RPG Program
def main():
        print("######################")
        print("#  Command Line RPG  #")
        print("######################\n")

        # Get user name and set up the character menu for user selection
        name = input('What is your name? \n')
        player.name = name
        heroesList = goodCharacters()
        characterMenu(heroesList)
        choice = characterValidation()
        setupCharacter(choice, heroesList, player)

        # Print the rules of the game for the user
        print('\n***** {} *****'.format(player.title))
        print('Good Luck, Get to Level 5 and Escape the Dungeon')
        print('There are 3 enemies lurking about')
        print('Gain experience by lowering their health to 0')
        print('You lose if you run out of health before level 5\n')

        # Method that displays the selected character's info
        player.playerStats()

        # Loop that continues until the user's characters hp reaches 0 or level reaches 5
        while player.level < 5 or player.hp > 0:
            playerTurn(player)
            player.update()
            enemyTurn(player)
            player.update()


#############
# Functions #
#############

# Function that reads character info from the friendlycharacters txt file
# and makes a list of Hero character objects
def goodCharacters():
    with open('friendlycharacters', 'r') as f:
        lines = f.readlines()
        f.close()
        knightInfo = lines[0].split()
        healerInfo = lines[1].split()
        mageInfo = lines[2].split()
    friends = []
    charKnight = Hero(knightInfo[0], knightInfo[1], knightInfo[2], int(knightInfo[3]))
    charHealer = Hero(healerInfo[0], healerInfo[1], healerInfo[2], healerInfo[3])
    charMage = Hero(mageInfo[0], mageInfo[1], mageInfo[2], mageInfo[3])
    friends.append(charKnight)
    friends.append(charHealer)
    friends.append(charMage)
    return friends

# Function that creates a list of Enemy objects
def badCharacters():
    enemies = []
    enemyBarbarian = Enemy("Barbarian", 15, 3, 50)
    enemyNinja = Enemy("Ninja", 10, 2, 30)
    enemyWarlock = Enemy("Warlock", 10, 1, 30)
    enemies.append(enemyBarbarian)
    enemies.append(enemyNinja)
    enemies.append(enemyWarlock)
    return enemies

# Function to display that character menu
def characterMenu(characters):
    print('\n{:12}{:8}{:10}{:10}'.format('Characters', 'Health', 'Strength', 'Magic'))
    print('-----------------------------------------------')
    selection = 1
    for char in characters:
        print('{}: {:10}{:10}{:8}{}'.format(str(selection), char.name, char.hp, char.str, char.mag))
        selection += 1

# Function to display the actions menu
def actionsMenu():
    print('Actions\n-------------')
    for act in actions:
        print('{}: {}'.format(act, actions[act]))
    print('')

# Function that takes the character selected from user and updates the Player object
def setupCharacter(choice, character, player):
    if choice == 1:
        knight = character[0]
        player.title = '{} the {}'.format(player.name, knight.name)
        player.maxhp = int(knight.hp)
        player.hp = int(knight.hp)
        player.str = int(knight.str)
        player.mag = int(knight.mag)
        return player
    elif choice == 2:
        healer = character[1]
        player.title = '{} the {}'.format(player.name, healer.name)
        player.maxhp = int(healer.hp)
        player.hp = int(healer.hp)
        player.str = int(healer.str)
        player.mag = int(healer.mag)
        return player
    elif choice == 3:
        mage = character[2]
        player.title = '{} the {}'.format(player.name, mage.name)
        player.maxhp = int(mage.hp)
        player.hp = int(mage.hp)
        player.str = int(mage.str)
        player.mag = int(mage.mag)
        return player

# Function that controls the actions a user can take
def playerTurn(player):
    print('#############')
    print('# YOUR TURN #')
    print('#############\n')
    actionsMenu()
    endTurn = False
    while endTurn == False:
        userAction = input('Enter the corresponding number to the Action you wish to take\n')
        if actionValidation(userAction):
            toDo = actions[int(userAction)]
            if toDo == 'search':
                print('{} decides to search the dungeon'.format(player.title))
                enemyList = badCharacters()
                randomEnemy = random.randint(0, 2)
                print('You have ran into a {}\n'.format(enemyList[randomEnemy].name))
                battleTime(player, enemyList[randomEnemy])
                player.update()
                endTurn = True
            elif toDo == 'camp':
                print('\n{} decides to camp\n'.format(player.title))
                if player.hp < player.maxhp:
                    print('Your health has been slightly restored')
                    healAmount = random.randint(1, 3)
                    if player.mag >= 2:
                        healAmount += 1
                    player.hp += healAmount
                if player.hp >= player.maxhp:
                    print('Your health is full')
                    player.hp = player.maxhp
                print('Health points: {} / {}\n'.format(player.hp, player.maxhp))
                endTurn = True
            elif toDo == 'stats':
                player.playerStats()
                actionsMenu()
            elif toDo == 'help':
                print('\n***** INFO *****')
                print('Search: Looks for the next room in the dungeon')
                print('Camp:   Restores a small amount of health')
                print('Stats:  Shows you your current player statistics')
                print('Exit:   Ends the program\n')
                actionsMenu()
            elif toDo == 'exit':
                sys.exit(0)

# Function that handles the computer/enemies turn
# Creates a random possibity of being seen/attacked by an enemy
def enemyTurn(player):
    print('################')
    print('# Enemies TURN #')
    print('################\n')
    enemyList = badCharacters()
    attackProbability = random.randint(1,100)
    if attackProbability >= 75:
        print("Enemy has spotted you! Prepare for battle\n")
        endTurn = False
        while endTurn == False:
            if player.level == 1:
                enemy = enemyList[2]
                battleTime(player, enemy)
                endTurn = True
            elif player.level == 2 or player.level == 3:
                enemy = enemyList[1]
                battleTime(player, enemy)
                endTurn = True
            elif player.level == 4:
                randEnemy = random.randint(0,2)
                enemy = enemyList[randEnemy]
                battleTime(player, enemy)
                endTurn = True
    elif attackProbability < 75:
        print('You managed to escape detection\n')
        if player.hp < player.maxhp:
            print('You regained 1 health point\n')
            player.hp += 1
    player.update()

# Function that handles the battle portion between the player and enemy object
def battleTime(player, enemy):
    while player.hp > 0:
        print('{} attacks you for {} damage'.format(enemy.name, enemy.str))
        enemy.attack(player)
        if player.hp <= 0:
            return False
        print('{} attacks {} for {} damage'.format(player.title, enemy.name, player.str))
        player.attack(enemy)
        if player.title == '{} the Healer'.format(player.name):
            healChance = random.randint(1,100)
            if healChance >= 50:
                print('You sapped 1 health from {}\n'.format(enemy.name))
                player.hp += 1
                enemy.hp -= 1
        elif player.title == '{} the Mage'.format(player.name):
            spellChance = random.randint(1,100)
            if spellChance >= 50:
                print('Your spell was strong and did 1 extra damage\n')
                enemy.hp -= 1
        if enemy.hp <= 0:
            print('Defeated the {}\n'.format(enemy.name))
            gainExperience(player, enemy)
            return True

def gainExperience(player, enemy):
    player.exp += enemy.exp
    if player.exp >= 100:
        print('You leveled up and restored your health\n')
        player.level += 1
        player.exp -= 100
        player.hp = player.maxhp
    if player.level == 5:
        print('CONGRATULATIONS!!!')
        print('{} made it safely out of the dungeon\n'.format(player.title))
        player.playerStats()
        with open('wins_losses', 'a') as f:
            f.write('{:15}: level {} - WIN\n'.format(player.title, player.level))
            sys.exit(0)





#################################
# VALIDATION and ERROR HANDLING #
#################################
def characterValidation():
    try:
        choice = int(input('\nSelect Character [Enter 1 - 3]: \n'))
        while (choice > 3 or choice < 0):
            print('\nOops, Enter 1 for Knight, 2 for Mage, and 3 for Healer')
            choice = int(input('Select Character [Enter 1 - 3]: \n'))
        return choice
    except ValueError:
        print('Oops, Enter 1 for Knight, 2 for Mage, and 3 for Healer')
        characterValidation()

def actionValidation(userAction):
    try:
        for act in actions:
            if int(userAction) == act:
                return True
        print("Oops, Enter 1 for search, 2 for camp, 3 for stats, 4 for help, 5 to exit\n")
    except ValueError:
        print("Oops, Enter 1 for search, 2 for camp, 3 for stats, 4 for help, 5 to exit\n")
        return False

main()