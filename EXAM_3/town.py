# Author: Anna Mikhailova
# Date: 10/28/21
# Course: COSC_001
# Purpose: Exam 3 Problem 1: Define a Town class that has four instance variables name, population, state and
# is_capital. The instance variable name is a string that stores the name of the Town,
# population is an integer that stores the population of the town, state is a string that
# stores the name of the state the town is located in and is_capital is a boolean value
# that indicates the town is the state capital.

class Town:
    def __init__(self, gname, gpop, gstate):
        self.name = gname  # string
        self.population = gpop  # integer
        self.state = gstate  # string
        self.is_capital = False

    def update_population(self, n):
        self.population = n  # integer

    def change_capital_status(self):
        self.is_capital = not self.is_capital

    def __str__(self):
        if self.is_capital:
            return self.name + ", " + self.state + ", " + str(self.population) + " *"
        else:
            return self.name + ", " + self.state + ", " + str(self.population)
