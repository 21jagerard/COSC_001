# Author: Vasanta
# Date: 11/08/2021
# Purpose: Queue class file
from collections import deque


class Queue:
    def __init__(self):
        # self.data = [] #Queue stores as python list
        self.data = deque()

    def enQ(self, val):
        # With python lists:O(1)
        # With deque: O(1)
        self.data.append(val)

    def deQ(self):
        # With python lists: O(n)
        # if len(self.data) > 0:
        #     val = self.data[0]
        #     del self.data[0]
        #     return val

        # With deque: O(1)
        if len(self.data) > 0:
            val = self.data.popleft()
            return val

        return None
