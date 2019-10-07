# Blackjack

# Instructions
To run the game in terminal type: 'python blackjack.py'

To run the test in terminal type: 'python test_blackjack.py'

The game is a single player blackjack game

# Design Choices:
The card and deck modules can also be used for other card games as well

The deck only takes up the previously used cards once the number of cards fall below MIN_NUMBER_CARDS_IN_DECK

The deck and hands store the cards as a list

When taking user inputs, the same question is repeated until the user gives a valid input

I chose to use python because it's an object oriented language and I'm very familiar with it

# TO DO
If I spent more than the recommended 3 hours on the game I would add more tests for the game such as:

    - To also test basic functionality of the game not just edge cases like empty deck and converting ace from 11 to 1

    - To test more of the game logic

- Make the game multiplayer
- Let the user specify how many decks they would like to use
- Implement splitting


