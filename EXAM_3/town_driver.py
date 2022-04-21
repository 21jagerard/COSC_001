# Author: Anna Mikhailova
# Date: 10/28/21
# Course: COSC_001
# Purpose: Exam 3 Problem 1 driver file: Create a driver file that creates a Town object (pick any town of your choice)
# and does the following on that object:
# 1. without directly calling __str__ method prints the string returned when
# __str__ method is called on the object created above.
# 2. changes the capital status for the object created above.
# 3. again, without directly calling __str__ method prints the string returned
# when __str__ method is called on the object created above to see if an
# asterisk is added at the end of the string.
# 4. updates the population of the town to 5000

from EXAM_3.town import Town

Boston = Town("Boston", 100000, "MA")
print(Boston)
Boston.change_capital_status()
print(Boston)
Boston.update_population(5000)
print(Boston)