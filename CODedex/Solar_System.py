# Write code below 💖 6/23/2025

"""
from random import sample as samp

famous_houses=['Stark', 'Targaryen', 'Baratheon', 'Greyjoy', 'Lannister' ]

example= samp(famous_houses,2)
print(f'Example:  {example}')
"""

from math import pi
from random import choice as ch
planets=['Mercury',
         'Venus',
         'Earth',
         'Mars',
         'Saturn']

random_planet=ch(planets)


if random_planet == 'Mercury':
    r=2440
elif random_planet == 'Venus':
    r=6052
elif random_planet =='Earf':
    r=6371
elif random_planet=='Mars':
    r=3309
elif random_planet=='Saturn':
    r=58232
else:
    print('Oops! ErroR!, ErRor!')

area= 4 * pi * r**2

print(f'Teh surface AE of {random_planet} es approximately {area:.2f} km^2')
                

#passed c
