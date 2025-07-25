# CODedex/pyi/numPY/notification.py
'''
* Author: TanB
* Created: 7/22/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import numpy as np

print(np.__version__)
#list[] array
#billz = [1337, 4200, 5000, 4350, 2400, 1234]

#numppy array
#billz = np.array([1337, 4200, 5000, 4350, 2400, 1234])

x = np.random.randint(3,43,size = 5)
print(x)
print(x[1])
print(x[0:3])


print('-' *10)

#2024-2019 MIAMI FL
cityz = np.array([487014, 455924, 450014, 439890, 442241, 441889])

print(cityz[1])#2023

print(cityz[0:6])#2024-2019

print(cityz[0]-cityz[4])
