#Author: Vasanta
#Date: 11/5/2021
#Purpose: Creating a linked list

from Lec24.node import Node

#Purpose: Create a singly linked list and return the head node reference
def build_ll(glist):
    if len(glist) == 0:
        return None

    head = Node(glist[0])
    n = head
    for i in range(1, len(glist)):
        new = Node(glist[i])
        n.next = new
        n = new

    return head

def print_ll(head):
    n = head
    while n != None:
        print(n, end="")
        n = n.next


h1 = build_ll([10, 5, 7, 8, 45, 7])
print_ll(h1)


#Purpose: Look for value in the linked list
#Parameters: head and val
#Return: Reference to node that has the value or None if value not in the list
def find_val(head, val):
    n = head
    while n != None:
        if n.data == val:
            return n
        n = n.next

    #return None #default return statement at the end


print("\nFind val:")
print(find_val(h1, 45))

def check_increasing(head):
    n = head
    while n.next != None:
        next_node = n.next
        if n.data > next_node.data:
            return False

        n = n.next

    return True


h2 = build_ll([10, 45, 167, 89, 342])
print(check_increasing(h2))