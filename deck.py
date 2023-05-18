from card import Card
import random

class Deck:
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self._cards = [Card(s, n) for s in suits for n in numbers]

    def shuffle(self):
        random.shuffle(self._cards)
