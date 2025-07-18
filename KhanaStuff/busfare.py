# KhanaStuff/busfare.py
'''
* Author: TanB
* Created: 7/9/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''


#my code
'''
age=int(input("How old are tu? "))

bus_fare=4.25

#kids ride free

is_kid = age < 5

if is_kid:
    print('Kids ride for free')
elif age > 50:
    print(f'elders have a discount. your price es {bus_fare-1}')
else:
    print('Teh bus fare is $' , str(bus_fare), '.')

'''


age=int(input("How old are tu? "))

bus_fare=4.25

is_kidz=age <5
fare_type=''
#kids ride free
if is_kidz:
    bus_fare=0
    fare_type='kids'
#senior gets a dollar off
elif age >= 60:
    bus_fare -=1
    fare_type='senior'


else:
    fare_type='standard'

print(f'the {fare_type} bus fair is $ {bus_fare}.  ')