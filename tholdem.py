import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [0, 0]

class Opponent:
    def __init__(self):
        self.bluff = random.randint(1, 10)
        self.hand = [0, 0]


class Deck:
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self._cards = [Card(s, n) for s in suits for n in numbers]
    
    def shuffle(self):
        random.shuffle(self._cards)

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

def printc(card):
    if (card.number != 10):
        print("----")
        print("|" + card.number + " |")
        print("----")
    else:
        print("----")
        print("|" + card.number + "|")
        print("----")     
 
def introduction():
    print("                        d8b")
    print("                        Y8P")
    print("")
    print(" .d8888b 8888b. .d8888b 88888888b.  .d88b.  ")
    print("d88P"       "88b88K     888888  88bd88  88b ")
    print("888     .d888888 Y8888b.888888  888888  888 ")
    print("Y88b.   888  888     X88888888  888Y88..88P ")
    print(" Y8888P Y888888  88888P'888888  888  Y88P ")

def player_info_gathering():
    name = input("What is your name? ")
    player = Player(name)
    return player

def player_introduction(player):
    print("Hello, " + player.name + ". Welcome to Texas Holdem.")
    print("The goal of Texas Holdem is to create the best combination of cards possible. These combinations are ranked such that they are less probable the strong they are.")
    print("Opponents have a 'bluff' rating.")
    print("The higher their 'bluff' rating, the more likely it is that they bluff a bad hand.")
    print("----------------------------------------------------------------------------------")
# Main Function

# Introduction ASCII & Player information gathering

introduction()
player = player_info_gathering()
player_introduction(player)


# Declaration of Deck

deck = Deck()

# Opponents Generation

opp_one = Opponent()
opp_two = Opponent()
opp_three = Opponent()
opp_four = Opponent()
opp_five = Opponent()

# Command Loop

while True: