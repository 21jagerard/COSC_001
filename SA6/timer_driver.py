# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/17/21
# Purpose: timer driver file; Finally, write a driver for the Timer class. It should start a timer at 01:30:00 and
# count it down to 00:00:00, printing to the console all the times between and including 01:30:00 and 00:00:00.

from SA6.timer import Timer
H = 1
M = 30
S = 0

timer1 = Timer(H, M, S)
while not timer1.is_zero():
    print(timer1)
    timer1.tick()
print(timer1)