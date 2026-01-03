import numpy as np 

n2dArry = np.array([[7,420,9,88,1337,69], [8,44,66,85,2558,4269]])

n1dArry = np.array([420,69,1337,7,True])

print(n2dArry[0][4])#rowxcolumn also [x, y]
print(f'es {n2dArry[0,2]}')
print(f'The second array of this 2darray xrow, and ycolumn {n2dArry[:, 3:7]}')

print(type(n2dArry))

print('***-----------------------------------------------------***')

# revers