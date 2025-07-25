# KhanaStuff/if_stuff.py
'''
* Author: TanB
* Created: 7/18/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff

days_of_the_week = input('What day of the week is it? ').lower()

if days_of_the_week == 'saturday' or days_of_the_week == 'sunday':
    print('WE are close')
elif days_of_the_week  in {'monday', 'tuesday' , 'wednesday', 'thursday', 'friday'}:
    print('We are open from 6am - 8pm')    
else:
    print('Enter a valid date') 
'''
import random

print('O' * 10)
"""
age=int(input('please enter age: '))

if age >=13:
    print('you\'re old enough')
else:
    print('sorry too young')
if age >=60:
    print('you get the senior discount')    
"""
"""
score = int(input('score: '))
if score >= 100:
    print('you win the grand prize')
elif score >= 70:
    print('you win a medium prize')
print('Thank you for playing')

print(score)
"""
purchase = 45
if purchase >= 50.0:
    purchase = purchase * .5
    print("You get half off your purchase!")
elif purchase >= 40.0:
    purchase = purchase - 10
    print("You get a $10 discount!")
else:
    print("No discount available for this purchase.")