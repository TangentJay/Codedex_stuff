# Codedex_stuff/edabit.py/ratio.py
'''
* Author: TanB
* Created: 6/30/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

#ratio multiplyer

def ratio():
    #input twoo numbers to make up teh ratio
    x=float(input('Entre num1: '))
    y=float(input('Entre num2: '))
    
    #ask for teh multiplier
    multiplier= float(input("Entre teh multiplier: "))

    #multiply both parts of teh ratio
    newx=x*multiplier 
    newy=y*multiplier

    #print teh results
    print(f'original ratio: {x}:{y}')
    print(f'Scaled ratio: {newx}:{newy}')

ratio()