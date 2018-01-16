
import sys

from heroes import *
# Player class inheriting from the Player class
class Player(Hero):
    def __init__(self, name, hp, str, mag):
        Hero.__init__(self, name, hp, str, mag)
        self.exp = 0
        self.maxhp = 0
        self.title = ''
        self.level = 1

    # Method to display current player information
    def playerStats(self):
        print('Current Player Stats\n---------------------')
        print('Title:    {}'.format(self.title))
        print('Health:   {}/{}'.format(self.hp, self.maxhp))
        print('Strength: {}'.format(self.str))
        print('Magic:    {}'.format(self.mag))
        print('Level:    {}'.format(self.level))
        print('Exp:      {}/100\n'.format(self.exp))

    # Method to handle updating hero's hp and if its 0
    # end the program and write the current player and player level to file
    def update(self):
        if self.hp <= 0:
            self.dead = True
            self.hp = 0
            print('Game Over. Better Luck Next Time\n')
            with open('wins_losses', 'a') as f:
                f.write('{:15}: level {} - Loss\n'.format(self.title, self.level))
                sys.exit(0)


