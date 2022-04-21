# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: You will now write a function that defines a part of bank ATM functionality.
# When you enter an amount to withdraw cash from the ATM the machine tries to minimize
# the number of currency notes(bills) it gives out. Let us assume the machine
# has only 20 dollar, 5 dollar and 1 dollar bills. Now your job is to define a function
# help_atm that takes an integer withdrawal_amount as parameter and prints the number
# of 20 dollar, 5 dollar and 1 dollar notes the ATM should give the customer.
#
# For example:
# If withdrawal_amount is 38 then the function should print:
# 1  20 dollar
# 3  5 dollar
# 3  1 dollar
# If withdrawal_amount is 30 then the function should print:
# 1  20 dollar
# 2  5 dollar

twenty_count = 0
five_count = 0
one_count = 0

def help_atm(left):
    global twenty_count, five_count, one_count
    if left >= 20:
        while left >= 20:
            twenty_count += 1
            left -= 20
    if (left >= 5) and (left < 20):
        while (left >= 5) and (left < 20):
            five_count += 1
            left -= 5
    if (left >= 1) and (left < 5):
        while (left >= 1) and (left < 5):
            one_count += 1
            left -= 1
    print("You will receive", twenty_count, "$20 bills,", five_count, "$5 bills, and", one_count, "$1 bills.")

withdrawal_amount = int(input("How much money would you like to withdraw?"))
help_atm(withdrawal_amount)

