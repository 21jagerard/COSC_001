# Author: Anna Mikhailova
# Date: 09/20/21
# Purpose: Another example for counting loop

n = 5
# 1 + 2 + 3 + 4 + ... + n

# sum = 0
# count = 0
#
# while count < n:
#     count +=1
#     sum += count
# print(sum)

sum = 0
count = 1
while count <= n:
    count += 1
    sum += count
print(sum)
