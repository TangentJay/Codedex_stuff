# CODedex/pyi/numPY/06Der_data.py
'''
* Author: TanB
* Created: 7/23/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#for _ in range(5):
 #   print(_)
import numpy as np
# 1D array: Hours on PC each day from Monday - Sunday
hr_on_pc = np.array([11, 9, 10, 9, 12, 12, 8])# mon-sun

#avg hours per day spent on pc
avg_hrs = np.average(hr_on_pc)
print(f'Avg hours spent on PC:, {avg_hrs} \n')


# difference between hours spent on monday and sunday 
diff = hr_on_pc[0] - hr_on_pc[6]
print(f'difference between monday und sunday: {diff}\n')


#total hrs in this week
total = np.sum(hr_on_pc)
print(f'total hrs I spent last week was {total} hrs or so.\n')


#max value and the index value
max = np.max(hr_on_pc)
amax = np.argmax(hr_on_pc)
print (max)
print(amax)

#min value and the index value
min = np.min(hr_on_pc)
amin = np.argmin(hr_on_pc)
print(min)
print(amin)

print(f'The max hours spent on teh PC was {max} hrs last week, and the minimum was {min} hrs')