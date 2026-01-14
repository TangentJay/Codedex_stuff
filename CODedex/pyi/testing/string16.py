# CODedex/pyi/testing/string16.py
'''
* Author: TanB
* Created: 8/14/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

import unittest

"""self.assertEqual(): Checks if two values are equal.
self.assertTrue() and self.assertFalse(): Verifies boolean conditions.
self.assertIn() and self.assertNotIn(): Checks for membership in a collection."""

import turtle

def reverse_string(s):
  
  return s[::-1]

def capitalize_string(s):

  return s.capitalize()

def is_capitalized(s):
  return s[0].isupper()

def zscore(d,m,s):
  return  (d-m)/s

# print(reverse_string('oops'))
# print(capitalize_string('bob'))
# print(is_capitalized('tom'))
# print(f'{zscore(13,3,7):.2f}')