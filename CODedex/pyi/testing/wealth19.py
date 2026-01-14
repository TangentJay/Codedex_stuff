# CODedex/pyi/testing/wealth19.py
'''
* Author: TanB
* Created: 8/17/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

class BankAccount:
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive')
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        
        self.balance -= amount

        