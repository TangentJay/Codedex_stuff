# projects/sorts.py
'''
* Author: TanB
* Created: 8/6/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import math
pim = [3,4,6]
for i in range(3):
    print( '| * | * |', pim)

print(len(pim))




def fun1():
   return fun(5,6,7)

def fun(x,y,z):
    return x*y-z


print(fun1())

print('lambda expression')

print(type(fun1))

my_fun = fun1

print(my_fun())

r = lambda j: j**3

print(r(3))

print(math.log2(8))
n = int(input('Please enter a number: '))
if n % 2 == 0:
    print('divisiable')
else: print( 'not visiable')    

