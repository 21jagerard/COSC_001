# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/18/21
# Purpose: card class file; There are four suits of cards: clubs, spades, diamonds, and hearts. In each suit, there are
# 13 card values: cards with numbers 1 through 10, the Jack (11), the Queen (12), and the King (13).
# A standard deck has 52 cards: one of each value, for each suit. (We ignore the Joker.)

class Card:
    def __init__(self, card, suit):
        self.card = int(card)
        self.suit = int(suit)

    def card_return(self):
        if self.card == 1:
            return "Ace"
        elif 2 <= self.card <= 10:
            return str(self.card)
        elif self.card == 11:
            return "Jack"
        elif self.card == 12:
            return "Queen"
        else:
            return "King"

    def suit_return(self):
        if self.suit == 1:
            return "clubs"
        elif self.suit == 2:
            return "spades"
        elif self.suit == 3:
            return "diamonds"
        else:
            return "hearts"

    def __str__(self):
        return self.card_return() + " of " + self.suit_return()
