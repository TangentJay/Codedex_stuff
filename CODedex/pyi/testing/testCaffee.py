# CODedex/pyi/testing/testCaffee.py
'''
* Author: TanB
* Created: 8/18/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''


import unittest
from  kaffee import kaffeeMenu

class TestKaffeeMenu(unittest.TestCase):

    def setUp(self):
        self.menu = kaffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('black_kaffee'), 3.69)


    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.get_price('nonexistent_item'))

    def test_add_item(self):
        self.menu.add_item('jello_kaffee', 4.20)
        self.assertEqual(self.menu.get_price('jello_kaffee'), 4.20)


if __name__ == '__main__':
    unittest.main()