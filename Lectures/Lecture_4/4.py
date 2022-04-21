# Author: Anna Mikhailova
# Date: 09/20/21
# Purpose: Demo while loops (accumulating)

limit = 24

# 1+2+3+4+... until reach 24, or cross 24
# count = 0
# sum = 0
#
# while sum < limit:
#     count += 1
#     sum += count
#
# print(count, sum)

count = 1
sum = 0

while sum < limit:
    sum += count
    count += 1

print(count -1)