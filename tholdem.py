import random

class Node:
    def __init__(self, player):
        self.player = player
        self.next = None

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, player):
        newNode = Node(player)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 0
        self.dealer = 1

class Opponent:
    def __init__(self, name):
        self.name = name
        self.bluff = random.randint(1, 10)
        self.hand = []
        self.money = 0
        self.dealer = 0


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
    if (card.suit == "spades"):
        print(" _____ ")
        print("|" + card.number + " .  |")
        print("| /.\ |")
        print("|(_._)|")
        print("|  |  |")
        print("|_____|")
    if (card.suit == "diamonds"):
        print(" _____ ")
        print("|" + card.number + " ^  |")
        print("| / \ |")
        print("| \ / |")
        print("|  .  |")
        print("|_____|")
    if (card.suit == "clubs"):
        print(" _____ ")
        print("|" + card.number + " _  |")
        print("| ( ) |")
        print("|(_'_)|")
        print("|  |  |")
        print("|_____|")
    if (card.suit == "hearts"):
        print(" _____ ")
        print("|" + card.number + "_ _ |")
        print("|( v )|")
        print("| \ / |")
        print("|  .  |")
        print("|_____|")

def player_info_gathering():
    name = input("What is your name? ")
    player = Player(name)
    return player

def flop(table, deck, deck_count):
    # Burn one card
    deck_count += 1
    table[0] = deck._cards[deck_count]
    deck_count += 1
    table[1] = deck._cards[deck_count]
    deck_count += 1
    table[2] = deck._cards[deck_count]
    deck_count += 1
    # Printing of cards
    printc(table[0])
    printc(table[1])
    printc(table[2])


def player_introduction(player):
    print("Hello, " + player.name + ". Welcome to Texas Holdem.")
    print("The goal of Texas Holdem is to create the best combination of cards possible. These combinations are ranked such that they are less probable the strong they are.")
    print("Opponents have a 'bluff' rating.")
    print("The higher their 'bluff' rating, the more likely it is that they bluff a bad hand.")
    print("----------------------------------------------------------------------------------")

def deal_cards(current, deck_count, deck):
    while current.player.dealer != 1:
        current.player.hand.append(deck._cards[deck_count])
        current = current.next
        deck_count = deck_count + 1
    current.player.hand.append(deck._cards[deck_count])

    current = table.head
    current = current.next
    # Phase two of dealing.
    while current.player.dealer != 1:
        current.player.hand.append(deck._cards[deck_count])
        current = current.next
        deck_count = deck_count + 1
    current.player.hand.append(deck._cards[deck_count])
# Main Function

# Introduction ASCII & Player information gathering

player = player_info_gathering()
player_introduction(player)


# Declaration of Deck

deck = Deck()

# Opponents Generation

opp_one = Opponent("opp_one")
opp_two = Opponent("opp_two")
opp_three = Opponent("opp_three")
opp_four = Opponent("opp_four")
opp_five = Opponent("opp_five")

# Allocation of Money for player and AI

player.money = int(input("How much money would you like to start with?"))
opp_one.money = player.money
opp_two.money = player.money
opp_three.money = player.money
opp_four.money = player.money
opp_five.money = player.money

# We start off with the player as the dealer.
# Declaring a circularly linked list to make a 'table' environment.

table = LinkedList()
table.insert(player)
table.insert(opp_one)
table.insert(opp_two)
table.insert(opp_three)
table.insert(opp_four)
table.insert(opp_five)
# Adding the circular link.
circular = table.head

while (circular.next):
    circular = circular.next
circular.next = table.head

# Flop, turn and river

flop_t_r = []


# Start of the command loop

deck_count = 0
current = table.head
current = current.next

while player.money > 0:
    # Dealing out of cards.
    deck.shuffle()
    print("Dealing phase:")
    deal_cards(current, deck_count, deck)

    # Now time to create flop


    break


