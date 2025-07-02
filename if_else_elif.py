# Codedex_stuff/if_else.py
'''
* Author: TanB
* Created: 6/27/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
'''
if test statement:
    body of if
elif test statement:
    body of efil
else:
    body of else    
'''

#python if elif und else statements
import random
#remember random.randint(a,b)
num=random.randint(-100,100)
#num=3
if num > 0: #test expression
    print('num is positive')#body condition
elif num ==0:
    print('num es 0')
else:      #no expession
    print('num es negative')
print(num)
