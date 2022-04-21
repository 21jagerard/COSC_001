#Author: Vasanta
#Date: 11/08/2021
#Purpose: Driver for stacks and queues

from Lec25.queue import Queue
from Lec25.stack import Stack

q = Queue()

q.enQ(25)
q.enQ(78)
q.enQ(10)

x = q.deQ()
print(x)

q.enQ(44)

s = Stack()

s.push(15)
s.push(20)
s.push(35)
s.push(4)

val = s.pop()
print(val)

s.push(10)
val = s.pop()
print(val)