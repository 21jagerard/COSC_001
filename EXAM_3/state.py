# Author: Anna Mikhailova
# Date: 10/28/21
# Course: COSC_001
# Purpose: Exam 3 Problem 2: Define a State class that has three instance variables name, capital and town_list.
# The instance variables name and capital are strings that store the name of the state
# and name of the capital town respectively. The instance variable town_list contains
# the references of Town objects and indicates the towns that are in this state.
# Assume that all towns in the state have a unique name and only one of the towns in
# the list is a state capital.

from EXAM_3.town import Town

class State:
    def __init__(self, gname, gtown_list, gcapital):
        self.name = gname  # string
        self.town_list = gtown_list  # list
        self.capital = gcapital  # capital

        for town in self.town_list:
            if town.name == gcapital:
                town.change_capital_status()

    def get_population(self):
        total_pop = 0
        for town in self.town_list:
            total_pop += town.population
        return total_pop

    def change_capital(self, gnew_capital):
        self.capital = gnew_capital  # string
        for town in self.town_list:
            if town.is_capital:
                town.change_capital_status()
            if town.name == gnew_capital:
                town.change_capital_status()

    def get_capital_town(self):
        for town in self.town_list:
            if town.is_capital:
                return town

    def __str__(self):
        return self.capital + ", " + self.name + ", " + str(self.get_population())
