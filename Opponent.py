import random

class Opponent:
    def __init__(self, name):
        self.name = name
        self.bluff = random.randint(1, 10)
        self.hand = []
        self.money = 0
        self.dealer = 0