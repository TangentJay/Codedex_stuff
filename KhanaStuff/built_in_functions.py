# Codedex_stuff/KhanaStuff/intro2.py
'''
* Author: TanB
* Created: 7/3/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import random
num=random.randint(1,100)
print('------------------')

print(min(49,5,55,68,1))

print(max(49,69))
print('------------')
print(num)
def hello():
    return 'raptor'

print (hello())
print('-------------------------')

#bob=input('SOmething  ')
#print(bob)
#type casting
#str(x): Returns the value x converted into a string. 
print(str(44))
print('---------------------')
#Int(x): Returnes the value converted into a interger. 
print(int('55'))
print('---------------')
#Float(x) Returns the value x converted into a float.
print(float('69'))
print('-------------------')
#bool(x) Returnes the value x converted to a boolean any zero value converts to false, and some value converts to true
print(bool(4))
print(bool(0))
print('-------------------')
#interger and floats 
#abs (x) returns the absoulte value of x

print(abs(-50))
print(abs(5))
print('--------------')
#round(x) returns the value x rounded to the nearest interger 

print(round(3.5))
print(round(3.4))
#round(x,y) returnes the number x rounded to the yth decimal place
print(round(6.9420,1))
print(round(6.9420,2))
print(round(6.9420,3))
print('---------------')
#strings
#len(x) returnes the number of characters in the string: inclueds all char,letter, num, symbols and spaces
print('-----------------')
print(len('exit'))
print(len('save as 9'))
print(len(""))
print('-----------------')

#min(x,y) returnes the lesser of the x and y values. The lesser string comes first in a case sensitive dictionary order 0-9 A-Z a-z
print(min('aArdvark','zebra'))
print(min('oosode', '4'))
print(min('bob','BOB'))
#max(x,y) returnes the greater of the x and y value The greater string comes last  in a case-sensitive dictionary order 0-9 A-Z a-z
print(max('aArdvark','zebra'))
print(max('oosode', '4'))
print(max('bob','BOB'))

