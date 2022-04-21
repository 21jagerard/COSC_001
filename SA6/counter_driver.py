# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/17/21
# Purpose: counter class driver

from test import Counter

limit = 25
counter1 = Counter(limit, 20, 4)

for i in range(limit):
    print(counter1)
    counter1.tick()

print("-----------")

counter2 = Counter(20, 15, 3)
print(counter2.tick())
print(counter2.get_value())
print(counter2)