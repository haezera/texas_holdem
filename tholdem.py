#####################################################################################
import random
from functions import *
from node import Node
from linkedlist import LinkedList
from player import Player
from opponent import Opponent
from deck import Deck
from card import Card

#####################################################################################

#####################################################################################

# Introduction ASCII & Player information gathering

player = player_info_gathering()
player_introduction(player)

# Declaration of Deck

deck = Deck()

# Opponents Generation

opp_one = Opponent("Amy")
opp_two = Opponent("Jack")
opp_three = Opponent("Dilara")
opp_four = Opponent("Lucas")
opp_five = Opponent("Jeff")

# Allocation of Money for player and AI

player.money = int(input("How much money would you like to start with?"))
opp_one.money = player.money
opp_two.money = player.money
opp_three.money = player.money
opp_four.money = player.money
opp_five.money = player.money
big_blind = player.money / 50
small_blind = big_blind / 2

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
pot = 0
current = table.head
current = current.next

while player.money > 0:
    # Small blind and big blind
    current.player.money -= small_blind
    pot += small_blind
    current.next.player.money -= big_blind
    pot += big_blind
    # Dealing out of cards.
    deck.shuffle()
    print("Dealing phase:")
    deal_cards(current, deck_count, deck, table)

    # Pre-flop betting
    printh(player)
    pot = preflop_bet(table, pot, player, big_blind)
    # Now time to create flop
    print("Pot: " + str(pot))
    flop_t_r = flop(flop_t_r, deck, deck_count)
    printh(player)
    pot = postflop_bet(table, pot, player, big_blind, flop_t_r) + pot
    print("Pot: " + str(pot))
    flop_t_r = turn(flop_t_r, deck, deck_count)
    printh(player)
    pot = postflop_bet(table, pot, player, big_blind, flop_t_r) + pot
    flop_t_r = river(flop_t_r, deck, deck_count)
    printh(player)
    pot = postflop_bet(table, pot, player, big_blind, flop_t_r) + pot

    break


