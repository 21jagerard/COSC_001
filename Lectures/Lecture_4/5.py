# Author: Anna Mikhailova
# Date: 09/20/21
# Purpose: Fibonacci

# 1,1,2,3,5,8,13,21,...

n = 5
f1 = 1
f2 = 1
count = 0

while count < n:
    print(f1)
    count += 1

    new = f1 + f2
    f1 = f2
    f2 = new

