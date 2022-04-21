# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/18/21
# Purpose: Recitation 4: account class file;

class Account:
    def __init__(self, initial_deposit, type):
        # takes an initial deposit and string type as parameters
        self.balance = int(initial_deposit)
        self.type = str(type)  # checking account CAN go negative, savings account CANNOT go negative
        self.overdraft = False

    def withdraw(self, withdrawal_amt):
        # takes an integer amount as parameter, returns true if successful, false if otherwise
        if self.type == "checking":
            self.balance -= withdrawal_amt
            if self.balance < 0:
                self.overdraft = True
            return True
        if self.type == "savings":
            if self.balance - withdrawal_amt < 0:
                return False
            else:
                self.balance -= withdrawal_amt
                return True

    def deposit(self, deposit_amt):
        # takes integer amount and adds to account balance; if balance >=0 overdraft is set to false
        self.balance += deposit_amt
        if self.balance >= 0:
            self.overdraft = False

    def __str__(self):
        # when called, should return a string type, balance, and overdraft statues of account
        return str(self.type) + ", " + str(self.balance) + ", " + str(self.overdraft)

