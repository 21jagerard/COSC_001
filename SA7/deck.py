# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/18/21
# Purpose: deck class file;

from SA7.card import Card
from random import randint

class Deck:
    def __init__(self):
        self.card_list = []

    def add_standard_cards(self):
        for i in range(1, 14):
            for j in range(1, 5):
                self.card_list.append(Card(i, j))
        return self.card_list

    def shuffle(self):
        # Fisher-Yates algorithm --> idk if we're allowed to use this, but I learned it when first learning python
        # for i in range(len(self.card_list)):
        #     j = randint(0, i + 1)
        #     temp = self.card_list[i]
        #     self.card_list[i] = self.card_list[j]
        #     self.card_list[j] = temp
        # return self.card_list
        for i in range(len(self.card_list)):
            j = randint(0, len(self.card_list) - 1)
            card = self.card_list.pop(j)
            self.card_list.append(card)

    def deal(self, n):
        hand = Deck()

        for i in range(n):
            if len(self.card_list) == 0:
                break
            hand.card_list.append(self.card_list.pop())

        return hand







