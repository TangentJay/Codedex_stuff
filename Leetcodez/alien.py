# Leetcodez/alien.py
'''
* Author: TanB
* Created: 8/1/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        
        orderInd = {c: i for i, c in enumerate(order)}

        for i in range(len(words) -1):
            w1, w2 = words[i], words[i + 1]
            print(f'comparing: {w1} vs {w2}]')

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False
                    break
        return True 


    

s = Solution()
print(s.isAlienSorted(['kepplez','billy', 'bob', 'ello'], 'acbdefghkijlmnopqrstuvwyxz' ))

