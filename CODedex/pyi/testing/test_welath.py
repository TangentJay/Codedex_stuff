# CODedex/pyi/testing/test_welath.py
'''
* Author: TanB
* Created: 8/17/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

import unittest
from wealth19 import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1337)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1337)
   
   
    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 1387)

    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw_positive_amount(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 1307)

    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(99999)

    def tearDown(self):
        self.account = None
            


if __name__=='__main__':
    unittest.main()