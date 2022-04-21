# Author: Anna Mikhailova
# Date: 09/20/21
# Purpose: Demo while loops (counting)

text = input("enter a number:")
n = int(text)

count = 0
while count < n:  # lets say n is 4
    print(count)  # 0, 1, 2, 3
    count += 1
