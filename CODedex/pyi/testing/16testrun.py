# CODedex/pyi/testing/16testrun.py
'''
* Author: TanB
* Created: 8/14/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

import unittest

import unittest

def add(a, b):
  return a + b

class TestAddition(unittest.TestCase):
  # Define the first unit test
  def test_add(self):
    result = add(4, 4)

    # Define the expected result
    expected_result = 7
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
  unittest.main()