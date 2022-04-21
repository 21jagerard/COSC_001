# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/18/21
# Purpose: Recitation 4: account driver file;

from Recitation_5.account import Account

my_account1 = Account(500, "checking")
my_account1.withdraw(200)
print(my_account1)
my_account1.deposit(200)
print(my_account1)
my_account1.withdraw(600)
print(my_account1)

my_account2 = Account(500, "savings")
my_account2.withdraw(200)
print(my_account2)
my_account2.deposit(200)
print(my_account2)
my_account2.withdraw(600)
print(my_account2)
