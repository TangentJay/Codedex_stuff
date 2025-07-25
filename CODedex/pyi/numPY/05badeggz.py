# CODedex/pyi/numPY/05badeggz.py
'''
* Author: TanB
* Created: 7/23/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#2d arrys 
#1 Diamnesion
import numpy as np

arr = np.array([4,2,0,1,3,3,7])

#2 diamension  array within an array
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arrav2 = np.array([[1,2,3],
                   [4,5,6]
                  ,[7,8,9]])#grid format

"""
The element at index 0 es [1,2,3],
The element at index 1 ist [4,5,6],
The element at index 2 es [7,8,9]
"""

print(arr[0])
print(arr2[0]) # to output each of the elements 
print(arr2[0][0]) #to output a specific element we use arr2[row][column]
print(arr2[1])
print(arr2[2])
print(arr2[0][1])
print(arr2[0][2])
print(arr2[1][0])
print(arr2[1][1])
print(arr2[1][2])
print(arr2[2][0])
print(arr2[2][1])
print(arr2[2][2])

egg_carton1 = np.array([[.89, .90, .83, .89, .97, .98],
                        [.95, .95, .89, .95, .23, .99]])

egg_carton2 = np.array([[.89, .95, .84, .92, .94, .93],
                      [.93, .95, .02, .03, .23, .99]])

egg_carton3 = np.array([[.83, .95, .89, .54, .37, .92],
                        [.98, .99, .19, .23, .89, .91]])

e1 = np.average(egg_carton1)
e2 = np.average(egg_carton2)
e3 = np.average(egg_carton3)


print(e1, e2, e3)