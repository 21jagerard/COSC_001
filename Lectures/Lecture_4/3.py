# Author: Anna Mikhailova
# Date: 09/20/21
# Purpose: Factorial

n = 5
# 1*2*3*4*5

count = 1
prod = 1

while count <= n:
    prod *= count
    count += 1

print(prod)