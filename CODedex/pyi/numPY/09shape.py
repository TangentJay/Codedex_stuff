# CODedex/pyi/numPY/09shape.py
'''
* Author: TanB
* Created: 7/24/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#go
#.shape returns a tuple contining numbers of elements each dimension has
import numpy as np


arr = np.array([[1,2,3,4],[5,6,7,8]])

print('*' *12)
print('*' *12)
print("  🦘 ")
print('*' *12)
print('*' *12)

print(arr.shape)

"""
The 1st dimension has 2 elements (for the rows).
The 2nd dimension has 4 elements (for the columns).

"""

arrR = np.array([1,2,3,4,5,6,7,8])
Rarr = arrR.reshape(2,4)

print(Rarr)


month_results = np.array([56, 100, 33, 0, 45, 45, 46, 34, 89, 180, 60, 45, 45, 44, 46, 45, 0, 0, 15, 90, 301, 197, 20, 60, 45, 45, 42, 45])
print('the shape is: ', np.shape(month_results))

weeks = month_results.reshape(4,7)

print(weeks)