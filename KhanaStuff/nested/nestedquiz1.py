# KhanaStuff/nested/nestedCon1.py
'''
* Author: TanB
* Created: 8/7/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import random
# d = int(input('Enter distance: '))
# tm = input('Enter mode of transportation: ')


# distance = d
# transport_mode = tm

# if distance < 3:
#     if transport_mode == 'walk':
#         print('You have enough time to walk there.')
    
#     print('\nit should be a short trip.')
# else:
#     print('\nyou should take the bus there.')
#-------------------------------------------------------
# points = int(input('enter points: '))
# status = input('enter status: ')
# if status == 'member':
#     if points >= 20:
#         print('you have enough points for a free book')
#     print ('Thank you for being a member!')

#----------------------------------------------------------
# inventory = 1

# if inventory > 0:
#     print('the item is in stock.')
#     purchase = input('purchase item: ')
#     if purchase == 'yes':
#         print('proceeding to checkout')
#     else:
#         print('thank you for browsing')
# else:
#     print('this item is currently out of stock.')
# --------------------------------------------------------------


# answer = input('hi, how can I elp you? ')
# if answer == 'reservations':
#     num_people = int(input('how many people? '))

#     if num_people >= 8:
#         print ('sorry. that exceeds our party limit.')
#     else:
#         print('reservation is booked')
# ___________________________________________________________

rc = random.choice(['sunny', 'rainy'])

weather = rc #input('what is the day like?: ')
trail_condition = input('trail conditions: ')

if weather == 'sunny':
    if trail_condition == 'dry':
        print(' it\'s a great day for hiking!') 
    else:
        print('conditions may be rough')
    print('time to get going!')

print(rc)