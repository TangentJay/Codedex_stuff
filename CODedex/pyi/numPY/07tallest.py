# CODedex/pyi/numPY/07tallest.py
'''
* Author: TanB
* Created: 7/24/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

import numpy as np

order = np.array([1337, 4200, 4321,1567])
print(order * .5)

#meters to feet
#m = ft * .3048
tallest_buiildings_ft = np.array([2717,2227,2073,1972,1966,1819,1776])

tallest_buiildings_m=tallest_buiildings_ft * .3048


tallest_buiildings_m_rounded = np.round(tallest_buiildings_m,2)

print(f'The tallest buildings in the world in feet: {tallest_buiildings_ft}')
print(f'The tallest buildings in the world in meters: {tallest_buiildings_m_rounded}')

