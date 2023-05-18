import random
from node import Node
from linkedlist import LinkedList
from player import Player
from opponent import Opponent
from deck import Deck
from card import Card

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
      
def straight_finder(full_hand):
    diff = 0
    if (len(full_hand) < 5):
        return False
    elif (len(full_hand) == 5):
        for i in range(1, len(full_hand)):
            diff = full_hand[i].number - full_hand[i-1].number
            print(diff)
            # Ace high straight, 1 -> 5
            if (diff != 1):
                if (i == len(full_hand) 
                and full_hand[i].number == 14
                and full_hand[0].number == 2):
                    return True
                else:
                    return False
    elif (len(full_hand) == 6):
        for i in range(1, len(full_hand)):
            diff = full_hand[i].number - full_hand[i-1].number
            if (diff != 1):
                # 6th number is not a straight, 1 -> 5 is a straight
                if i == len(full_hand):
                    return True
                # There is a 5th number blocking the ace straight. The 6th number would be 14. 
                elif (i == len(full_hand) - 1
                and full_hand[0].number == 2
                and full_hand[i + 1].numbver == 14):
                    return True
                else:
                    return False 
            else:
                return True
    elif (len(full_hand) == 7):
        for i in range(1, len(full_hand)):
            diff = full_hand[i].number - full_hand[i-1].number
            if (diff != 1):
                # 6th or 7th card - still constitutes a straight 1 -> 5
                if (i == len(full_hand)
                or i == len(full_hand) - 1):
                    return True
                # Example [2, 3, 4, 5, 7, 9, 14] = Ace high straight 1 2 3 4 5 
                elif (i == len(full_hand) - 2
                and full_hand[i + 2] == 14
                and full_hand[0] == 2):
                    return True
                else:
                    return False 
            # All 7 numbers constitute a straight
            else:
                return True
    return True
            

def flop(table, deck, deck_count):
    # Burn one card
    deck_count += 1
    table.append(deck._cards[deck_count])
    deck_count += 1
    table.append(deck._cards[deck_count])
    deck_count += 1
    table.append(deck._cards[deck_count])
    deck_count += 1
    # Printing of cards
    print("Table:")
    printc(table[0])
    printc(table[1])
    printc(table[2])

def printh(player):
    print("Your hand:")
    printc(player.hand[0])
    printc(player.hand[1])

def player_introduction(player):
    print("Hello, " + player.name + ". Welcome to Texas Holdem.")
    print("The goal of Texas Holdem is to create the best combination of cards possible. These combinations are ranked such that they are less probable the strong they are.")
    print("Opponents have a 'bluff' rating.")
    print("The higher their 'bluff' rating, the more likely it is that they bluff a bad hand.")
    print("----------------------------------------------------------------------------------")

def deal_cards(current, deck_count, deck, table):
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

def hand_strength(player, table):
    i = 0

    full_hand = []
    full_hand.append(player[0])
    full_hand.append(player[1])

    for i in range(len(table)):
        full_hand.append(player[i])

    # Sort into 'ascending' order
    full_hand.sort()

    # Royal flush
        
def hand_strength_preflop(player):
    # Consider the hand strength at the table
    suited = 0
    high_pair = 0
    high_card = 0
    low_pair = 0
    if player.hand[0].suit == player.hand[1].suit:
        suited = 1
        if player.hand[0].number == player.hand[1].number:
            if (player.hand[0].number == 10 
            or player.hand[0].number == 'J'
            or player.hand[0].number == 'Q'
            or player.hand[0].number == 'K'
            or player.hand[0].number == 'A'):
                high_pair = 1
            else:
                low_pair = 1
    elif player.hand[0].number == player.hand[0].number:
        if (player.hand[0].number == 10 
        or player.hand[0].number == 'J'
        or player.hand[0].number == 'Q'
        or player.hand[0].number == 'K'
        or player.hand[0].number == 'A'):
            high_pair = 1
        else:
            low_pair = 1
    elif (player.hand[0].number == 10 
    or player.hand[0].number == 'J'
    or player.hand[0].number == 'Q'
    or player.hand[0].number == 'K'
    or player.hand[0].number == 'A'):
        high_card = 1
    if (high_card == 1):
        print("High card")
    elif (high_pair == 1 and suited == 1):
        print("Suited high pair")
    elif (low_pair == 1 and suited == 1):
        print("Suited low pair")
    elif (high_pair == 1):
        print("High pair")
    elif (low_pair == 1):
        print("Low pair")
    else:
        print("Bad hand")


def ai_bet_decision(opponent, big_blind):
    # First consider the amount of big blinds they have
    amnt_of_bbs = opponent.money / big_blind

def preflop_bet(table, pot, player):
    current = table.head # Dealer
    flag = current.next.next
    current = current.next.next.next # First person after big blind
    while current != flag:
        if current == player:
            player_bet = int(input("How much would you like to bet? (0 for nothing)"))
            while player_bet > player.money:
                print("Too large of a bet! Your current money is " + player.money + ".")
                player_bet = int(input("How much would you like to bet? (0 for nothing)"))
            pot += player_bet
            current.player.money -= player_bet
    


    # Adding probabilities and bluff effect. No bluffing pre-flop, that's stupid.
    # Perhaps a percentage of the pool v.s their cash should be taken into context. 

card_one = Card("hearts", 3)
card_two = Card("hearts", 4)
card_three = Card("hearts", 5)
card_four = Card("hearts", 6)
card_five = Card("hearts", 7)
card_six = card

if straight_finder([card_one, card_two, card_three, card_four, card_five]) == True:
    print("True")
else:
    print("False")