# Leetcodez/ifelse.py
'''
* Author: TanB
* Created: 7/31/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import random
def odd_even(n):
    if n % 2:
         return 'odd num'
    else:  
         return 'even num'
    

def old_age(age):
    if age < 16: return 'child'
    elif age < 50: return 'yung person'
    else:  return 'old person'

def times(x,y): return x*y

print(odd_even(6))

print(old_age(44))

num = 42

eve_odd = 'even' if num % 2 ==0 else 'odd'
print(eve_odd)

r=random.randint(10, 120)

age = 'even' if r % 2 == 0 else 'odd'
print(age)
print (r)

print(times(4,5))

def sale_hotdogz(n):
    if n < 5: return n * 100
    elif n< 10: return n * 95
    else:  return n * 90

print(sale_hotdogz(2))
    # your code here

def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)

print(sale_hotdogs(2))