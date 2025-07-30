# projects/algo.py
'''
* Author: TanB
* Created: 7/25/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

#binary search spin off
def CPU_guess():
    low = 1
    high = 100
    while low <= high:
        guess = (low + high) // 2
        print('Is teh #', guess, '?')
        user = input("Enter 'low', 'high', or 'correct': ")

        if user == 'correct':
            print('GG, dood.')
            return
        elif user == 'low':
            low = guess + 1
        else:
            high = guess - 1

CPU_guess()