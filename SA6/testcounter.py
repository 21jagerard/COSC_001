# Counter.py
# Create a counter.
# CS 1 Intro to Programming and Computation
# By Caitlyn Tabors
# October 15, 2019


class Counter:
    def __init__(self, limit, initial=0, min_digits=4):
        self.limit = limit
        self.value = initial
        self.min_digits = min_digits

    def get_value(self):
        return int(self.value)

    def __str__(self):
        length = len(str(self.value))
        difference = self.min_digits - length
        if difference <= 0:
            return str(self.value)
        padded_zeros = '0' * difference
        result = padded_zeros + str(self.value)
        return result

    def tick(self):
        self.value -= 1
        if self.value < 0:
            self.value = self.limit - 1
            self.get_value()
            return True
        else:
            return False
