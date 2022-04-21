# Author: Anna Mikhailova
# Date: 10/28/21
# Course: COSC_001
# Purpose: Exam 3 Problem 3: Define a Country class that has two instance variables name and state_list. The
# instance variable name is a string and state_list is a list of State objects that indicates the states in the country.

from EXAM_3.town import Town
from EXAM_3.state import State

class Country:
    def __init__(self, gname, gstate_list):
        self.name = gname  # string
        self.state_list = gstate_list  # list of state objects

    def get_population(self):
        total_pop = 0
        for state in self.state_list:
            total_pop += state.get_population()
        return total_pop

    def print_states_info(self):
        for state in self.state_list:
            print(state)