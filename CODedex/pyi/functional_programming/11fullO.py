# CODedex/pyi/functional_programming/11fullO.py
'''
* Author: TanB
* Created: 8/9/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
def impure_squared(number):
    result = number ** 2
    print('The square of', number, 'is', result)

    return result

def pure_squared(number):
    
    return number ** 2


impure_squared(4)
print(pure_squared(4))

import math
def circleA(raidus):
    
    area = math.pi *(raidus ** 2)
    return area

print(circleA(3))

with open('ex.txt', 'r', encoding='utf=8', newline='') as file:
    print(file.read())

