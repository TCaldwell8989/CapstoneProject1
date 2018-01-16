
from characters import *

class Hero(Character):
    def __init__(self, name, hp, str, mag):
        Character.__init__(self, name, hp, str)
        self.mag = mag