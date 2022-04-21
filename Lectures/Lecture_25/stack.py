# Author: Vasanta
# Date: 11/08/2021
# Purpose: Stack class file
from collections import deque


class Stack():
    def __init__(self):
        # self.data = [] #Storing stack elements in Python list
        self.data = deque()

    def push(self, val):
        # With python lists:O(1)
        # With deque: O(1)
        self.data.append(val)

    def pop(self):
        # With python lists: O(1)
        # With deque: O(1)
        if len(self.data) > 0:
            val = self.data.pop()
            return val

        return None
