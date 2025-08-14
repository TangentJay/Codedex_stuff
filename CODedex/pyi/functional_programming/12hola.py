# CODedex/pyi/functional_programming/12hola.py
'''
* Author: TanB
* Created: 8/10/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#Higher order functions

def apply_operation(operation, number):
    results=[]
    for num in number:
        results.append(operation(num))
    return results

def double(x):
    return(x * 2)

num_lst = [1,2,3,4,5]

double_numbers = apply_operation(double, num_lst)

print(f'Original um: {num_lst}')
print(f'double num: {double_numbers}')
