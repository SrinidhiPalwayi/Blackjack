# Constants
import math
import random

CARD_RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

CARD_SUIT = ("\u2660", "\u2662", "\u2663",  "\u2661") # spades, diamonds, club, heart

FACE_CARD_VALUE = 10
NUM_CARDS = 52


class Card(object):
    # each individual card
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " " + self.suit


class Deck(object):

    def __init__(self):
        self.cards = []
        for rank in CARD_RANKS:
            for suit in CARD_SUIT:
                self.cards.append(Card(rank, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            # if there's no more cards left start a new deck
            # never should actually hit this case when playing a hand if the minimum number of cards left in the deck
            # is set high enough
            self.__init__()
            return self.cards.pop()






class Hand(object):
    def __init__(self):
        self.cards = []
        self.num_aces = 0 # aces are special need to handle being 1 or 11
        self.cur_value = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.rank.isdigit():
            self.cur_value += int(card.rank)
        elif card.rank != "A":
            # if it's a face card
            self.cur_value += FACE_CARD_VALUE
        else:
            # if it's ace
            self.cur_value += 11
            self.num_aces += 1

        while self.cur_value > 21 and self.num_aces > 0:
            # reduce the ace value to 1
            self.cur_value -= 10
            self.num_aces -= 1

    def show(self, partial=False):
        # if partial is True don't show the first card. This is used for the dealer
        hand = ""
        for count, card in enumerate(self.cards):
            if count == 0 and partial:
                hand += "<Hidden Card> \n"
            else:
                hand += card.rank + " " + card.suit + "\n"
        if not partial:
            print(hand[:-1]) # don't want the last new line
            print("The total value is: " + str(self.cur_value) + "\n")
        else:
            print(hand)

    def __str__(self):
        hand = ""
        for card in self.cards:
            hand += card.rank + " " + card.suit + "\n"
        return hand




