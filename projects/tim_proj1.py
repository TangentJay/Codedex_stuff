# projects/tim_proj1.py
'''
* Author: TanB
* Created: 7/18/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#tech with tim frfr
print('timmy!')

name = input('What ist your name? ')
print(f'Hello, {name}, Lets play!')

ready = input('yes or no? ').lower()

if  ready == 'yes' or ready == 'y':
    print('We will play a little game!')

    direction = input('left or right? ').lower()
    if direction == 'left':
        print('you turn left and find yourself facing a portal.')
        choice = input('enter the portal or turn back? ')
        if choice == 'enter the portal' or choice == 'enter':
            print('you find yourself transported into a some dink cave with just enough light to make out very close objects')
    elif direction == 'right':
        print('We have decided to go up the right staircase')
    else:
        print('Not a valid option!')



else:
    print('That is too bad!')

