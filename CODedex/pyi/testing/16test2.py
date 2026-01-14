# CODedex/pyi/testing/16test2.py
'''
* Author: TanB
* Created: 8/14/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

for i in range(3):
    for j in range(3):
        print('#', end='')
    print()    
    
for i in range(3):
    print('#' *3)

# scores = []
# for i in range(3):
#     score = get('score: ')
#     score.append(score)

# avg = sum(scores) / len(scores)

import unittest

class MyTestCase(unittest.TestCase):
  def test_addition(self):
    result = 2 + 3
    self.assertEqual(result, 5)       # Verify that 2 + 3 equals 5

  def test_string_length(self):
    text = 'Hello, World!'
    self.assertEqual(len(text), 13)   # Verify string length

  def test_text_contains_word(self):
    text = 'Hello, World!'
    self.assertTrue('Hell0' in text)  # Verify that 'Hello' is in the text
    self.assertIn('World', text)      # Verify that 'World' is in the text

if __name__ == '__main__':
  unittest.main()


