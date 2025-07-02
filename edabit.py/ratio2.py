# Codedex_stuff/edabit.py/ratio2.py
'''
* Author: TanB
* Created: 6/30/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
def ratio(x,y,multiplier):
    newx=x*multiplier
    newy=y*multiplier
    return newx,newy

#ask user for input
x=float(input('Entre first number: '))
y=float(input('Entre second number: '))
multiplier=float(input('Entre teh multiplies: '))

#get results
scaled_ratio=ratio(x,y,multiplier)

#print teh ratio
print(f'Scaled ratio: {scaled_ratio[0]} : {scaled_ratio[1]}')
