# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/17/21
# Purpose: counter class file; Your first task is to define a class Counter for a counter that counts down.
# When it gets down to 0 and counts down again, it wraps back to a limit, minus 1.
# For example, if the limit is 60, the counter’s value is 0, and it counts down, its next value is 59.

class Counter:
    # The parameters are the counter’s limit (60 in the example above), an initial value, and a minimum number of digits
    # (explained below). If the initial value supplied as a parameter is between 0 and limit–1, then that’s the
    # counter’s initial value. Otherwise, an error message is printed and the counter’s initial value is limit–1.
    def __init__(self, limit, initial=0, min_digits=1):
        self.limit = limit
        self.current_val = initial
        self.min_digits = min_digits

        # error message if initial value supplied is not between 0 and limit-1
        if initial < 0 or initial >= limit:
            self.current_val = limit - 1
        # print("Unsupported initial value. Initial value has been set to", initial)

    def get_value(self):
        # just returns the counter’s value, as an int
        return int(self.current_val)

    def __str__(self):
        # returns the counter’s value, as a string. If the counter’s value would print with fewer than the min_digits
        # parameter supplied to the __init__ method, then the string contains min_digits characters, padded on the left
        # with zeros. For example, if min_digits is 4 and the counter’s value is 15,
        # then the __str__ method should return the string 0015.
        current_val = str(self.current_val)
        if len(str(current_val)) < self.min_digits:
            zeroes = "0" * (self.min_digits - len(current_val))
            current_val = zeroes + current_val
        return current_val

    def tick(self):
        # decrements the counter’s value, but if the value would go negative, then it becomes limit–1.
        # For example, if the counter’s limit is 12 and its current value is 0, then after calling tick,
        # the counter’s value should be 11. This method also returns to its caller a boolean value indicating
        # whether it wrapped around, i.e., did the value wrap from 0 back to limit–1.
        # True means that it wrapped, False means that it did not.
        self.current_val -= 1
        if self.current_val < 0:
            self.current_val = self.limit - 1
            return True
        return False



