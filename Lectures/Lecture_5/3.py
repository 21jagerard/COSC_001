# Author: Anna Mikhailova
# Date: 09/22/21
# Purpose: Demo functions with while and if loops

# Purpose: print out the first n even fibonacci numbers
# Parameters: integer n that tells us how many even fibonacci numbers to print
def even_fibs(n):
    count = 0
    f1 = 1
    f2 = 1

    print("The first", n, "even Fibonacci numbers are:")
    while count < n:
        if f1 % 2 == 0:
            print(f1)
            count += 1

        new = f1 + f2
        f1 = f2
        f2 = new


x = int(input("How many even Fibonacci numbers do you want?"))
even_fibs(x)
