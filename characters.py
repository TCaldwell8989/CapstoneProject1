
class Character(object):
    def __init__(self, name, hp, str):
        self.name = name
        self.hp = hp
        self.str = str
        self.dead = False

    def attack(self, other):
        other.hp -= self.str
        if other.hp < 0:
            other.hp = 0
        print("{:8} Health: {}\n".format(other.name, other.hp))







