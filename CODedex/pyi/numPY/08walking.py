# CODedex/pyi/numPY/08walking.py
'''
* Author: TanB
* Created: 7/24/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

"""
.min() Return the minimum value of an array.
.max() Return the maximum value of an array.
.sum() Return the total sum of an array's values.
.average() Return the average value of an array.
"""

import numpy as np


temperatures = np.array([[50, 51, 54, 59, 59,53, 54, 51],
                         [45, 50, 38, 44, 40, 46, 43, 39]])

print(np.min( temperatures))
print(np.max(temperatures))
print(np.sum(temperatures))
print(np.average(temperatures))

#axis
# axis=0 : operation goes across the coloumns
# axis=1 : operation goes across the rows ,
axis0 = np.sum(temperatures, axis=0)
axis1 = np.min(temperatures, axis=1)

print(axis0)
print(axis1)

steps = np.random.randint(3000,10000,size=5)

print(steps)


print('Miniumu steps taken es: ', np.min(steps))
print('maximum number of steps: ', np.max(steps))
print('sum of steps taken: ',  np.sum(steps))
print('average number of steps: ',np.average(steps))

