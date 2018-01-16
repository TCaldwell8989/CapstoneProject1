
import sys

from heroes import *

class Player(Hero):
    def __init__(self, name, hp, str, mag):
        Hero.__init__(self, name, hp, str, mag)
        self.exp = 0
        self.maxhp = 0
        self.title = ''
        self.level = 1

    def playerStats(self):
        print('Current Player Stats\n---------------------')
        print('Title:    {}'.format(self.title))
        print('Health:   {}/{}'.format(self.hp, self.maxhp))
        print('Strength: {}'.format(self.str))
        print('Magic:    {}'.format(self.mag))
        print('Level:    {}'.format(self.level))
        print('Exp:      {}/100\n'.format(self.exp))

    def update(self):
        if self.hp <= 0:
            self.dead = True
            self.hp = 0
            print('Game Over. Better Luck Next Time\n')
            with open('wins_losses', 'a') as f:
                f.write('{:15}: level {} - Loss\n'.format(self.title, self.level))
                sys.exit(0)


