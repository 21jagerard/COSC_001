# counter_test_harness.py
# to test counter.py
# By Caitlyn Tabors
# October 15, 2019

from SA6.testcounter import Counter

counter1 = Counter(60, 59, 4)

counter2 = Counter(50, 45, 4)


print(counter1.get_value())

print(counter2.tick())
