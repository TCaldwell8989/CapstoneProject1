from characters import *
# Hero class inheriting from Character class
class Hero(Character):
    def __init__(self, name, hp, str, mag):
        Character.__init__(self, name, hp, str)
        self.mag = mag