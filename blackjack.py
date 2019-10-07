# Imports
import traceback
import os
import sys
from cards import Hand, Deck, Card

# Constants
DEALER_CONSTANT = 17
GOAL_CONSTANT = 21
MIN_NUMBER_CARDS_IN_DECK = 15

def ask_how_much_money(question, cur_money=sys.maxsize):
    while True:
        input_money = input(question)
        try:
            money = int(input_money.strip())
        except ValueError:
            print("You must enter an positive integer \n")
        else:
            if money < 0:
                print("You must enter a positive integer \n")
            if money > cur_money:
                print("You must enter a positive integer less than " + str(cur_money) + "\n" )
            else:
                return money

def new_round():
    while True:
        action = input("Would you like to play another round \n" +
                       "1. [P]lay \n" +
                       "2. [Q]uit \n")
        if action in ["1", "p", "P"]:
            return True
        if action in ['2', 'Q', 'q']:
            return False
        else:
            print("Please make a selection using 1 or 2")


def win_statement(player, value):
    print(player + " won with a value of " + str(value) + "\n")


def lose_statement(player, value):
    print(player + " lost with a value of " + str(value) + "\n")


def play_round(deck):

    playerHand = Hand()
    dealerHand = Hand()

    playerHand.add_card(deck.deal())
    playerHand.add_card(deck.deal())

    dealerHand.add_card(deck.deal())
    dealerHand.add_card(deck.deal())

    print("The dealer has: ")
    dealerHand.show(partial=True)

    print("You have: ")
    playerHand.show()


    while True:
        action = input("Do you want to \n" +
                       "1. [H]it \n" +
                       "2. [S]tand \n")
        if action in ["1", "h", "H"]:
            playerHand.add_card(deck.deal())
            print("You have: ")
            playerHand.show()
            if playerHand.cur_value == GOAL_CONSTANT:
                win_statement("You", playerHand.cur_value)
                return playerHand, dealerHand, deck
            if playerHand.cur_value > GOAL_CONSTANT:
                lose_statement("You", playerHand.cur_value)
                return playerHand, dealerHand, deck

        if action in ['2', 'S', 's']:
            while dealerHand.cur_value < DEALER_CONSTANT:
                dealerHand.add_card(deck.deal())
                dealerHand.show(partial=True)
            if dealerHand.cur_value > GOAL_CONSTANT:
                print("The dealer has: ")
                dealerHand.show()
                lose_statement("Dealer", dealerHand.cur_value)

            return playerHand, dealerHand, deck
        else:
            print("Please make a selection using 1 or 2")


def main():
    print("Hi! Welcome to the Blackjack table. Let's see if you can beat the dealer")
    money = ask_how_much_money("How much money do you want to start with? You must enter a positve integer \n")
    round = 1
    deck = Deck()
    while (money > 0):
        print("Round " + str(round))
        print("Currently you have " +str(money) + " money")
        if new_round():
            bet = ask_how_much_money("How much money do you want to bet? \n", money)
            if len(deck.cards) < MIN_NUMBER_CARDS_IN_DECK:
                # reshuffle the cards, and start off with a full deck if have less than 10 cards
                deck = Deck()
            playerHand, dealerHand, deck = play_round(deck)
            if playerHand.cur_value == GOAL_CONSTANT or dealerHand.cur_value > GOAL_CONSTANT:
                money += bet
            elif playerHand.cur_value > GOAL_CONSTANT:
                money -= bet
            elif playerHand.cur_value > dealerHand.cur_value:
                win_statement("You", playerHand.cur_value)
                money += bet
            else:
                lose_statement("You", playerHand.cur_value)
                money -= bet
            round += 1
        else:
            print("You have left the game with " + str(money) + " money")
            return
    print("You have run out of money")
    return


if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt as e:
        raise e
    except SystemExit as e:
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        os._exit(1)


