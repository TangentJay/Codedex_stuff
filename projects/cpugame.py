# projects/cpugame.py
'''
* Author: TanB
* Created: 7/27/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

def guess_pc():
    low = 1
    high = 100
    while low <= high:
        guess = (low + high) //2
        print(f'ist teh #: {guess} ?')
        user = input ("entre 'lower', 'higher', or 'correct' : ").lower()

        if user =='higher':
            low = guess - 1
        elif user == 'lower':
            high = guess + 1
        elif user == 'correct':
            print('GG, dood')
            break
        else:
            print('Not a valid input!')        


guess_pc()