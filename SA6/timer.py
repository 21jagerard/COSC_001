# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/17/21
# Purpose: timer class file; Your next task is to define a class Timer for a 24-hour hours:minutes:seconds timer that
# counts down. It must have instance variables that reference Counter objects for the hours, minutes, and seconds.

from test2 import Counter

class Timer:
    # creates a timer whose initial values for its hours, minutes, and seconds are given by the parameters.
    # This method must create three Counter objects and save the references given back by the Counter constructors
    # in instance variables for the Timer object. If any of the values given for hours, minutes, or seconds
    # is out of range, then the initial value used should be the value that the corresponding Counter object would use.
    def __init__(self, hours, minutes, seconds):
        self.h = Counter(24, hours, 2)
        self.m = Counter(60, minutes, 2)
        self.s = Counter(60, seconds, 2)

    def __str__(self):
        # returns a string giving the timer’s current time, in the format hh:mm:ss. That is, two digits for the hours,
        # followed by a colon, followed by two digits for the minutes, followed by a colon,
        # followed by two digits for the seconds.
        time = str(self.h) + ":" + str(self.m) + ":" + str(self.s)
        return time

    def tick(self):
        if self.s.tick():
            if self.m.tick():
                self.h.tick()

    def is_zero(self):
        # returns a boolean that is True if the timer currently reads 00:00:00.
        if self.h.get_value() == 0 and self.m.get_value() == 0 and self.s.get_value() == 0:
            return True
        return False
