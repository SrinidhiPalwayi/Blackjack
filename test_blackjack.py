import unittest

from blackjack import *
from cards import *


class DeckTests(unittest.TestCase):
    def test_inital_size(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), NUM_CARDS)

    def test_draw(self):
        deck = Deck()
        orig_size = len(deck.cards)
        card1 = deck.deal()
        self.assertNotIn(card1,deck.cards)
        self.assertEqual(orig_size-1, len(deck.cards))

    def test_shuffle(self):
        deck_one = Deck()
        deck_two = Deck()
        self.assertNotEqual(deck_one, deck_two)

    def test_create_new_deck(self):
        deck = Deck()
        for i in range(NUM_CARDS):
            deck.deal()
            self.assertEqual(NUM_CARDS-i-1, len(deck.cards))

        deck.deal()
        self.assertEqual(NUM_CARDS-1, len(deck.cards))


class HandTest(unittest.TestCase):
    def test_ace_value_switch(self):
        test_player = Hand()
        test_player.add_card(Card("A", "\u2662"))
        test_player.add_card(Card("5", "\u2662"))
        self.assertEqual(test_player.cur_value, 16)
        test_player.add_card(Card("9", "\u2661"))
        self.assertEqual(test_player.cur_value, 15)




if __name__ == '__main__':
    unittest.main()



