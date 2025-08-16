# projects/temp_converter.py
'''
* Author: TanB
* Created: 8/14/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
# Celsius to Fahrenheit: F = (C * 9/5) + 32 or F = (C * 1.8) + 32
def celsius_to_f(celsius):
    """convert celsius to fahrenheit"""
    return celsius * (9/5) +32

#Fahrenheit to Celsius: C = (F - 32) * 5/9 
def fahrenheit_to_c(fahrenheit):
    """convert fahrenheit to celsius"""
    return (fahrenheit - 32) * 5/9

print(celsius_to_f(20))

print(fahrenheit_to_c(68))