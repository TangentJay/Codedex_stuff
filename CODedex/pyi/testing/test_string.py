# CODedex/pyi/testing/test_string.py
'''
* Author: TanB
* Created: 8/14/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import unittest
from string16 import reverse_string, capitalize_string, is_capitalized, zscore


"""self.assertEqual(): Checks if two values are equal.
self.assertTrue() and self.assertFalse(): Verifies boolean conditions.
self.assertIn() and self.assertNotIn(): Checks for membership in a collection."""



class TestString(unittest.TestCase):
    def test_reverse_string(self):

        
        self.assertEqual(reverse_string('oops'), 'spoo')
    
    def test_capitalize_string(self):
        self.assertEqual(capitalize_string('bob'),'Bob')

    def test_is_capitalized(self):
        self.assertTrue(is_capitalized('Tom'))

    def test_zscore(self):
       z = zscore(13,3,7)
       self.assertAlmostEqual(z,1.43, places=2)     
    


    
if __name__ == '__main__':
    unittest.main() 