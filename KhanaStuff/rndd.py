# KhanaStuff/rndd.py
'''
* Author: TanB
* Created: 8/20/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

import random

r = random.randint(1,100)

for r in range(r):
    print(r)


print('Try your luck at the lucky dice game!')
print(f'you rolled a {r}!')
if r < 50:
    again = random.randint(1,69)
    print(f'Here we go again {again}')
else: print('gg')

while r <=60:
    print(f'reroll {(r)}')
    r = random.randint(1,100)

print('gg',r)


#Team has 20% chance of winning , 30% chnce of loss and 50% chance of a tie

foos = random.randint(1,10)


if foos ==1 or foos ==2: 
    match_end = 'win'
elif foos <= 5: match_end = 'loss'
else: match_end = 'tied'

print(f'The score es {foos}, and the results of the match is {match_end}')