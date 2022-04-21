# Author: Anna Mikhailova
# Date: 10/28/21
# Course: COSC_001
# Purpose: Exam 3 Problem 3: Create a driver file that creates a Country object for the USA, with at least two states
# added to its state_list. The drive should also include code that calls the methods
# get_population and print_states_info .

from EXAM_3.town import Town
from EXAM_3.state import State
from EXAM_3.country import Country

Boston = Town("Boston", 100000, "MA")
Cambridge = Town("Cambridge", 80000, "MA")
Brookline = Town("Boston", 2000, "MA")
MA = State("MA", [Boston, Cambridge, Brookline], "Boston")

Manhattan = Town("Manhattan", 200000, "NY")
Albany = Town("Albany", 10000, "NY")
Syracuse = Town("Syracuse", 13000, "NY")
NY = State("NY", [Manhattan, Albany, Syracuse], "Albany")

USA = Country("USA", [MA, NY])
print(USA.get_population())
USA.print_states_info()
