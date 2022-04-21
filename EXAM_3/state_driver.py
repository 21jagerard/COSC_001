# Author: Anna Mikhailova
# Date: 10/28/21
# Course: COSC_001
# Purpose: Exam 3 Problem 2 driver file: Create a driver file that creates a State object
# (pick any state of your choice) with at least three Town objects in its town_list.
# The driver should also include code that calls the methods get_population, change_capital, get_capital_town,
# and __str__ methods defined in the State class .

from EXAM_3.town import Town
from EXAM_3.state import State

Boston = Town("Boston", 100000, "MA")
Cambridge = Town("Cambridge", 80000, "MA")
Brookline = Town("Boston", 2000, "MA")
Newton = Town("Boston", 17000, "MA")

MA = State("MA", [Boston, Cambridge, Brookline, Newton], "Boston")
print(MA)
print(MA.get_capital_town())
print(MA.get_population())
MA.change_capital("Cambridge")
print(MA)
print(MA.get_capital_town())