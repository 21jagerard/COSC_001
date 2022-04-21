# Author: Anna Mikhailova
# Date: 11/15/21
# Course: COSC_001
# Purpose: Linked list deletion

from Lectures.Lecture_28.node import Node

def ll_remove(head, val):
    if head.date == val:
        head = head.next
        return head

    p = None
    n = head

    while n != None:
         if n.data == val:
             p.next = n.next
             return head

         p = n
         n = n.next
    return head

def build_ll(glist):
    if len(glist) == 0:
        return None

    head = Node(glist[0])
    n = head
    for i in range(1, len(glist)):
        n.next = new
        n = new

    return head

def print_ll(head):
    n = head
    while n != None:
        print(n, end="")
        n = n.next

def ll_insert(head, val, af_val):
    n = head
    while n != None:
        if n.data == af_val:
            new = Node(val)
            new.next = n.next
            n.next = new

        n = n.next

h1 = build_ll([10, 5, 7, 8, 45, 72])
print_ll(h1)
print("\n")
h1 = ll_remove(h1, 10)
print_ll(h1)

ll_insert(h1, 25, 8)
print_ll(h1)
