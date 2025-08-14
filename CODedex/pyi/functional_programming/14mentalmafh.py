# CODedex/pyi/functional_programming/14mentalmafh.py
'''
* Author: TanB
* Created: 8/11/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
ns = sorted(numbers)

even_loopz = []
for num in numbers:
    if num % 2 ==0:
        even_loopz.append(num)

odd_nums = [num for num in ns if num % 2 != 0]
even_nums = [num for num in ns if num % 2 == 0] 

print(f'original numbers are: {numbers}')
print(f'Sorted order is:  {ns}')
print(f'even numbers are: {even_nums}')
print(f'odd numbers are {odd_nums}')
