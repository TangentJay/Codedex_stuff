a='hello' + " " + str(42)
print(f' sup  {a}') 

import random
dice=[1,2,3,4,5,6]
print(random.choices(dice, k=2))

age=int(input('whatz age: '))
if age>16:
    print("You may pass")
elif age <16 and age > 12:
    print("Can see pg moviez")
else:
    print('Can only see kidz stuff')
    
print(' -------------------')
print(f'|{age}     tu age    {age}|')
print(' -------------------')