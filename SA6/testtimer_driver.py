# timer_test_harness.py
# to test timer.py
# By Caitlyn Tabors
# October 15, 2019

from SA6.testtimer import Timer

timer = Timer(1, 30, 0)

while True:
    print(timer.tick())