from characters import *
# Enemy class inheriting from Character class
class Enemy(Character):
    def __init__(self, name, hp, str, exp):
        Character.__init__(self, name, hp, str)
        self.exp = exp