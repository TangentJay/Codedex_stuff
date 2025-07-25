# CODedex/pyi/numPY/11titanic.py
'''
* Author: TanB
* Created: 7/24/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

"""
.shape
.reshape
.arange
"""

import numpy as np


passengers = np.array([
   [1, 0, 3, 22],
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])

#passengers[:, 0] 

"""Passenger id (1 to 50)
Survived: 0 for no and 1 for yes.
Passenger class: 1 for Upper, 2 for Middle, 3 for Lower.
Age: 0-74"""
ages = passengers[:, 3]

minAge = np.min(ages)
maxAge = np.max(ages)
avgAge = np.mean(ages)
yngPassId = passengers[np.argmin(ages),0]
oldPassId = passengers[np.argmax(ages),0]
pasSurv = passengers[:, 1]
percentSur = np.sum(pasSurv)/ len(pasSurv)*100
classes = passengers[:, 2]

#the shape of the data array
print(f'The shap of teh array ist:  {np.shape(passengers)}')
#avg age of passengers
print(f'Average age is: {avgAge}')
# youngest and oldest age and their ID
print(f'Youngest person was: {minAge}, und their ID was: {yngPassId}')
print(f'Oldest person was: {maxAge}, and their ID was {oldPassId}')

#percent of people who lived
print(f'The precent of people who lived: {percentSur}%')


for ppl in [1,2,3]:
    live = (classes == ppl)
    #total in this class
    total_cls = np.sum(live)
    #num of furvivors
    survCls = np.sum(pasSurv[live])
    #we calculate
    percentage = survCls / total_cls * 100

    print(f'class tier {ppl}: {percentage}% survived')
