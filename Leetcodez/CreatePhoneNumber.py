# Leetcodez/CreatePhoneNumber.py
'''
* Author: TanB
* Created: 7/28/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import random

r = [random.randint(1,100) for _ in range(10) if random.randint(1,100) % 2 == 0]
print(r)