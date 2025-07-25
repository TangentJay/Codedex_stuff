# projects/timproj2.py
'''
* Author: TanB
* Created: 7/19/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''


operand = (input('number 1: '))
sign = input('sign: ')
operand_2 = (input('number 2: '))
results = ''


if sign == '+':
    results = float(operand) + float(operand_2)
elif sign == '-':
    results = float(operand) - float(operand_2)   
elif sign == '*':
    results = float(operand) * float(operand_2) 
elif sign == '/':
    results = float(operand) / float(operand_2) 
elif sign == '//':
    results = float(operand) // float(operand_2)
elif sign == '%':
    results = float(operand) % float(operand_2)             
#subtraction = operand - operand2
#multiplication = operand * operand2




print(results)


"""
def addition(a,b):2
    addition = a+b
    return addition

print(addition(4,5))
"""