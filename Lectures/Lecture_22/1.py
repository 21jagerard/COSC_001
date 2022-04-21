# Author: Anna Mikhailova
# Date: 11/01/21
# Purpose: Towers of Hanoi

def toh(source, dest, spare, n):
    if n == 0:
        return

    toh(source, spare, dest, n-1)
    print("Move disk", n, "from peg", source, "to peg", dest)
    toh(spare, dest, source, n-1)

toh("A", "B", "C", 4)