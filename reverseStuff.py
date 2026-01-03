#Just reverse stuff in pratice

#10/28/2025
import numpy as np
#10/30/2025
import matplotlib.pyplot as plt
# [::-1] =[start:stop:step] means start at the end and move backwards.

#EXample
print('yoh') 
print('yoh'[1::-1])

bob = [7,420,66,42,69,1337]

q = [48, 34, 6, 30, 13, 33]
j = 3,420
jj = np.arange(6,42)
npq = np.array(q)

print(npq)
print(jj)

val = 4,9,6,45,88,69,99
plt.title('bob')
plt.hist(val, bins=10)
plt.xlabel('hi')
plt.ylabel('adios')
plt.show()
plt.clf()

plt.hist(val, bins = 69)
plt.show()
plt.clf()

plt.scatter(val)
plt.show()
plt.clf()