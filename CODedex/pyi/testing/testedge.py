# CODedex/pyi/testing/testedge.py
'''
* Author: TanB
* Created: 8/15/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

import unittest
from edg318 import get_sqrt, divide

class testEddge(unittest.TestCase):
    def test_get_sqrt(self):
        self.assertEqual(get_sqrt(144),12)
    
    def test_get_sqrt_n(self):
        with self.assertRaises(ValueError):
            get_sqrt(-1)

    def test_divide(self):
        self.assertEqual(divide(144,12),12) 

    def test_divide_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(144,0)    

if __name__ == '__main__':
    unittest.main()