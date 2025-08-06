# code_task/frequency_map.py
'''
* Author: TanB
* Created: 7/30/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
frequency_map = {}

n = 1337420

while n > 0:
    digit = n % 10

    if digit not in frequency_map:
        frequency_map[digit] = 1
    else:
        frequency_map[digit] += 1
    n = n //10

print('frequencies:', frequency_map)