# timer.py
# Create a timer.
# CS 1 Intro to Programming and Computation
# By Caitlyn Tabors
# October 15, 2019

from SA6.testcounter import Counter

class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hour = Counter(hours)
        self.minute = Counter(minutes)
        self.second = Counter(seconds)

    def __str__(self):
        if len(str(self.hour)) == 2:
            hour_digits = str(self.hour)
        else:
            hour_digits = str("0" + str(self.hour))
        if len(str(self.minute)) == 2:
            minute_digits = str(self.minute)
        else:
            minute_digits = str("0" + str(self.minute))
        if len(str(self.second)) == 2:
            second_digits = str(self.second)
        else:
            second_digits = str("0" + str(self.second))
        result = str(hour_digits + ":" + minute_digits + ":" + second_digits)
        return result

    def tick(self):
        if int(self.second) < 0:
            self.minute -= 1
            self.second = 59
        else:
            self.second -= 1
        if int(self.minute) < 0:
            self.hour -= 1
            self.minute = 59
        else:
            self.minute -= 1

    def is_zero(self):
        return self.second == 0 and self.minute == 0 and self.hour == 0
