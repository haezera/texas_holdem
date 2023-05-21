import random
from node import Node
from linkedlist import LinkedList
from player import Player
from opponent import Opponent
from deck import Deck
from card import Card
from collections import Counter

###################################################################################################

###################################################################################################

def printc(card):
    if (card.suit == "spades"):
        print(" _____ ")
        print("|" + str(card.number) + " .  |")
        print("| /.\ |")
        print("|(_._)|")
        print("|  |  |")
        print("|_____|")
    if (card.suit == "diamonds"):
        print(" _____ ")
        print("|" + str(card.number) + " ^  |")
        print("| / \ |")
        print("| \ / |")
        print("|  .  |")
        print("|_____|")
    if (card.suit == "clubs"):
        print(" _____ ")
        print("|" + str(card.number) + " _  |")
        print("| ( ) |")
        print("|(_'_)|")
        print("|  |  |")
        print("|_____|")
    if (card.suit == "hearts"):
        print(" _____ ")
        print("|" + str(card.number) + "_ _ |")
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
            # Ace high straight, 1 -> 5
            if (diff != 1):
                if (i == len(full_hand) - 1 
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
                if i == 1:
                    first_mark = 1
                    continue
                elif i == len(full_hand):
                    full_hand.pop(i)
                    return True
                # There is a 5th number blocking the ace straight. The 6th number would be 14. 
                elif (i == len(full_hand) - 2
                and full_hand[0].number == 2
                and full_hand[5].number == 14):
                    full_hand.pop(i)
                    return True
                else:
                    return False 
                
    elif (len(full_hand) == 7):
        for i in range(1, len(full_hand)):
            diff = full_hand[i].number - full_hand[i-1].number
            if (diff != 1):
                if i == 1:
                    continue
                if i == 2:
                    continue
                # 6th or 7th card - still constitutes a straight 1 -> 5
                elif (i == len(full_hand) - 1
                or i == len(full_hand) - 2):
                    return True
                # Example [2, 3, 4, 5, 7, 9, 14] = Ace high straight 1 2 3 4 5 
                elif (i == len(full_hand) - 3
                and full_hand[i + 2] == 14
                and full_hand[0] == 2):
                    full_hand.pop(i)
                    full_hand.pop(i + 1)
                    return True
                else:
                    return False 
            # All 7 numbers constitute a straight
    return True


def straight_modifier(full_hand):
    diff = 0
    first_mark = 0
    second_mark = 0
    if (len(full_hand) < 5):
        return full_hand
    elif (len(full_hand) == 5):
        for i in range(1, len(full_hand)):
            diff = full_hand[i].number - full_hand[i-1].number
            # Ace high straight, 1 -> 5
            if (diff != 1):
                if (i == len(full_hand) - 1 
                and full_hand[i].number == 14
                and full_hand[0].number == 2):
                    return full_hand
                else:
                    return full_hand
    elif (len(full_hand) == 6):
        for i in range(1, len(full_hand)):
            diff = full_hand[i].number - full_hand[i-1].number
            if (diff != 1):
                print(full_hand[5].number)
                # 6th number is not a straight, 1 -> 5 is a straight
                if i == 1:
                    first_mark = 1
                    continue
                elif i == len(full_hand):
                    full_hand.pop(i)
                    return full_hand
                # There is a 5th number blocking the ace straight. The 6th number would be 14. 
                elif (i == len(full_hand) - 2
                and full_hand[0].number == 2
                and full_hand[5].number == 14):
                    full_hand.pop(i)
                    return full_hand
                else:
                    return full_hand
                
    elif (len(full_hand) == 7):
        for i in range(1, len(full_hand)):
            diff = full_hand[i].number - full_hand[i-1].number
            if (diff != 1):
                if i == 1:
                    first_mark = 1
                    continue
                if i == 2:
                    second_mark = 1
                    continue
                # 6th or 7th card - still constitutes a straight 1 -> 5
                elif (i == len(full_hand) - 1
                or i == len(full_hand) - 2):
                    return full_hand
                # Example [2, 3, 4, 5, 7, 9, 14] = Ace high straight 1 2 3 4 5 
                elif (i == len(full_hand) - 3
                and full_hand[i + 2] == 14
                and full_hand[0] == 2):
                    full_hand.pop(i)
                    full_hand.pop(i + 1)
                    return full_hand
                else:
                    return full_hand
            # All 7 numbers constitute a straight
    if (first_mark == 1):
        full_hand.pop(0)
    if (second_mark == 1):
        full_hand.pop(1)
    return full_hand


def flush_finder(full_hand):
    counter = 0
    for i in range(1, len(full_hand)):
        if full_hand[i].suit == full_hand[i-1].suit:
            counter += 1
    if counter == 5:
        return True
    else:
        return False


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
    return table

def turn(table, deck, deck_count):
    # Burn one card
    deck_count += 1
    table.append(deck._cards[deck_count])
    print("Table:")
    printc(table[0])
    printc(table[1])
    printc(table[2])
    printc(table[3])
    return table

def river(table, deck, deck_count):
    # Burn one card
    deck_count += 1
    table.append(deck._cards[deck_count])
    print("Table:")
    printc(table[0])
    printc(table[1])
    printc(table[2])
    printc(table[3])
    printc(table[4])
    return table


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
    

def full_house(full_hand):
    value_list = []
    three_count = 0
    two_count = 0
    for i in range(0, len(full_hand)):
        value_list.append(full_hand[i].number)
    c = Counter(value_list)
    for j in c.values():
        if (j == 3):
            three_count += 1
        if (j == 2):
            two_count += 1
    
    if (three_count >= 1 and two_count >= 1):
        return True

    return False


def four_of_a_kind(full_hand):
    value_list = []
    for i in range(0, len(full_hand)):
        value_list.append(full_hand[i].number)
    c = Counter(value_list)
    for j in c.values():
        if (j == 4):
            return True
    return False


def three_of_a_kind(full_hand):
    value_list = []
    for i in range(0, len(full_hand)):
        value_list.append(full_hand[i].number)
    c = Counter(value_list)
    for j in c.values():
        if (j == 3):
            return True
    return False


def two_pair(full_hand):
    value_list = []
    pair_counter = 0
    for i in range(0, len(full_hand)):
        value_list.append(full_hand[i].number)
    c = Counter(value_list)
    for j in c.values():
        if (j == 2):
            pair_counter += 1
    if (pair_counter >= 2):
        return True
    return False


def pair(full_hand):
    value_list = []
    for i in range(0, len(full_hand)):
        value_list.append(full_hand[i].number)
    c = Counter(value_list)
    for j in c.values():
        if (j == 2):
            return True
    return False


def hand_strength(player, flop_t_r):
    i = 0
    strength = 0
    full_hand = []
    full_hand.append(player[0])
    full_hand.append(player[1])

    for i in range(1, len(flop_t_r)):
        full_hand.append(flop_t_r[i])

    # Sort into 'ascending' order
    full_hand.sort(key = lambda x: x.number)

    # Royal flush
    if straight_finder(full_hand) == True:
        full_hand = straight_modifier(full_hand)
        if (flush_finder(full_hand) == True):
            if (full_hand[0].number == 10
            and full_hand[4].number == 14):
                strength = 10

    # Straight flush
    elif straight_finder(full_hand) == True:
        full_hand = straight_modifier(full_hand)
        if (flush_finder(full_hand) == True):
            strength = 9

    # Four of a kind
    elif four_of_a_kind(full_hand) == True:
        strength = 8

    # Full House
    elif full_house(full_hand) == True:
        strength = 7
    
    # Flush
    elif flush_finder(full_hand) == True:
        strength = 6
    
    # Straight
    elif straight_finder(full_hand) == True:
        full_hand = straight_modifier(full_hand)
        strength = 5
    
    # Three of a kind
    elif three_of_a_kind(full_hand) == True:
        strength = 4

    # Two pair
    elif two_pair(full_hand) == True:
        strength = 3

    # Pair
    elif pair(full_hand) == True:
        strength = 2
    
    # High Card
    else:
        strength = 1

    return strength
                  
def hand_strength_preflop(player):
    # Consider the hand strength at the table
    suited = 0
    high_pair = 0
    high_card = 0
    low_pair = 0
    strength = 0
    if player.hand[0].suit == player.hand[1].suit:
        suited = 1
        if player.hand[0].number == player.hand[1].number:
            if (player.hand[0].number == 10 
            or player.hand[0].number == 11
            or player.hand[0].number == 12
            or player.hand[0].number == 13
            or player.hand[0].number == 14):
                high_pair = 1
            else:
                low_pair = 1
    elif player.hand[0].number == player.hand[0].number:
        if (player.hand[0].number == 10 
        or player.hand[0].number == 11
        or player.hand[0].number == 12
        or player.hand[0].number == 13
        or player.hand[0].number == 14):
            high_pair = 1
        else:
            low_pair = 1
    elif (player.hand[0].number == 10 
    or player.hand[0].number == 11
    or player.hand[0].number == 12
    or player.hand[0].number == 13
    or player.hand[0].number == 14):
        high_card = 1

    if (high_pair == 1):
        strength = 5
    elif (low_pair == 1):
        strength = 4
    elif (suited == 1):
        strength = 3
    elif (high_card == 1):
        strength = 2
    else:
        strength = 1
    return strength


def ai_bet_decision(opponent, big_blind, table):
    # First consider the amount of big blinds they have
    amnt_of_bbs = opponent.money / big_blind
    opp_h_strength = 0
    bluff_decision = 0
    # Define the strength of their hand + consider their monetary position
    # A three of a kind and above is pretty strong. But this should be accounted for. 
    opp_h_strength = hand_strength(opponent.hand, table)

    # First need to decide if they are a big bluffer or not. 
    bluff_decider = random.randint(1, 10)
    if bluff_decider <= opponent.bluff:
        bluff_decision == 1
        return True
    else:
        # Consider monetary strength
        # Tight
        if (amnt_of_bbs < 15):
            if (opp_h_strength >= 4):
                return True
            else:
                return False
        # Loose
        else:
            if (opp_h_strength >= 2):
                return True
            else:
                return False



def preflop_bet(table, pot, player, big_blind):
    current = table.head # Dealer
    flag = current.next.next # Big Blind
    current = current.next.next.next # First person after big blind
    while current != flag:
        if current.player.fold == 1:
            current = current.next
        elif current.player == player:
            player_bet = int(input("How much would you like to bet? (0 for nothing, -1 for fold) "))
            if (player_bet == -1):
                player.fold = 1
            else:
                while player_bet > player.money:
                    print("Too large of a bet! Your current money is " + player.money + ".")
                    player_bet = int(input("How much would you like to bet? (0 for nothing) "))
                pot += player_bet
                current.player.money -= player_bet
                current = current.next
        else:
            opp_h_strength = hand_strength_preflop(current.player)
            if (opp_h_strength == 2):
                print(current.player.name + " bets " + str(big_blind))
                current.player.money -= big_blind
                pot += big_blind
            elif (opp_h_strength >= 3):
                print(current.player.name + " bets " + str(big_blind * (current.player.bluff / 10 + 1)))
                current.player.money -= big_blind * (current.player.bluff / 10 + 1)
                pot += big_blind * (current.player.bluff / 10 + 1)
            else:
                print(current.player.name + " folds")
                current.player.fold = 1
            current = current.next
    if current.player.fold != 1:
        if current.player == player:
            player_bet = int(input("How much would you like to bet? (0 for nothing, -1 for fold) "))
            if (player_bet == -1):
                print("You fold")
                player.fold = 1
            else:
                while player_bet > player.money:
                    print("Too large of a bet! Your current money is " + player.money + ".")
                    player_bet = int(input("How much would you like to bet? (0 for nothing) "))
                pot += player_bet
                current.player.money -= player_bet
                current = current.next
        else:
            opp_h_strength = hand_strength_preflop(current.player)
            if (opp_h_strength == 2):
                print(current.player.name + " bets " + str(big_blind))
                current.player.money -= big_blind
                pot += big_blind
            elif (opp_h_strength >= 3):
                print(current.player.name + " bets " + str(big_blind * (current.player.bluff / 10 + 1)))
                current.player.money -= big_blind * (current.player.bluff / 10 + 1)
                pot += big_blind * (current.player.bluff / 10 + 1)
            else:
                print(current.player.name + " folds")
                current.player.fold = 1
            current = current.next
    return pot

def postflop_bet(table, pot, player, big_blind, flop_t_r):
    flag = table.head
    current = flag.next
    while (current != flag):
        if current.player.fold == 1:
            pass
        elif current.player == player:
            player_bet = int(input("How much would you like to bet? (0 for nothing, -1 for fold) "))
            if (player_bet == -1):
                print("You fold")
                player.fold = 1
            else:
                while player_bet > player.money:
                    print("Too large of a bet! Your current money is " + player.money + ".")
                    player_bet = int(input("How much would you like to bet? (0 for nothing) "))
                pot += player_bet
                current.player.money -= player_bet
                current = current.next
        else:
            if ai_bet_decision(current.player, big_blind, flop_t_r) == True:
                pot -= big_blind * (current.player.bluff / 10 + 1)
            current = current.next
    if current.player.fold != 1:
        if current.player == player:
            player_bet = int(input("How much would you like to bet? (0 for nothing, -1 for fold) "))
            if (player_bet == -1):
                player.fold = 1
            else:
                while player_bet > player.money:
                    print("Too large of a bet! Your current money is " + player.money + ".")
                    player_bet = int(input("How much would you like to bet? (0 for nothing) "))
                pot += player_bet
                current.player.money -= player_bet
                current = current.next
        else:
            if ai_bet_decision(current.player, big_blind, flop_t_r) == True:
                print(current.player.name + " bets " + str(big_blind * (current.player.bluff / 10 + 1)))
                pot += big_blind * (current.player.bluff / 10 + 1)
            current = current.next
    return pot