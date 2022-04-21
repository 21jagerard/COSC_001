# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Using a return statement to build is_prime

# def is_prime(n):
#     if n == 1:
#         print(False)
#     else:
#         factor = 2
#
#         while factor < n:
#             if n % factor == 0:
#                 print(False)
#                 break
#
#             factor += 1
#
#         if factor == n:
#             print(True)
#
# is_prime(15)

# ----------------------------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------------------------

# def is_prime(n):
#     if n == 1:
#         print("1 is a special number :)")
#         return
#     factor = 2
#
#     while factor < n:
#         if n % factor == 0:
#             print(n, "is not prime")
#             break
#
#         factor += 1
#
#     if factor == n:
#         print(n, "is prime")
#
# is_prime(7)

# ----------------------------------------------------------------------------------------------------------------------
# Prints out all of the prime numb ers from 1 to 100
# ----------------------------------------------------------------------------------------------------------------------

def is_prime(n):
    if n == 1:
        return False

    factor = 2

    while factor < n:
        if n % factor == 0:
            return False

        factor += 1
    # if factor ==n:
    return True

i = 1
while i < 100:
    check = is_prime(i)
    if check == True:
        print(i)
    i +=1