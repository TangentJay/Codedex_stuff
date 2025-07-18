# KhanaStuff/iftst.py
'''
* Author: TanB
* Created: 7/9/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

'''
FF=input('WHich FF game do you  like? ')
FFXIII='Nein'

if FF=='FFXIII':
    FFXIII=input('Did you also play 13-2 and LR?: ')
print(f'you fav FF game is {FF} and if you picked ff13, you might have said {FFXIII}')
'''

#--------------------------------------------------------------------------------------------

ground_status='unwatered'
print('Checking plant.')

if ground_status != 'watered':
    ground_status ='watered'
    print('Plant watered')
print('Watering check complete.')

fuel=1.5
print('starting trip. ')

if fuel < 7.0:
    fuel =fuel +5.5
    print('Refueled at stop 1.')

if fuel < 8.0:
    fuel = fuel + 4.5
    print('refueled at stop 2')    