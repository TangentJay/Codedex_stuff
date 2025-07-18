# projects/guess_my_num.py
'''
* Author: TanB
* Created: 7/11/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

#We will import random

import random
print('Choose a difficulty lvl: Ez, medium, oder Hard. ')
difficulty = input('Enter difficulty: ' ).lower


#We will set num range and max attempts one can guess
if difficulty =='ez':
    max_number = 20
    max_attempts = 10
    print('you picked ez mode!')

elif difficulty == 'medium':
    max_number = 50
    max_attempts = 7
    print('Medium it es')

else:
    max_number = 100
    max_attempts = 10
    print('man mode!')    

# generate teh secret number
secret_number = random.randint(1, max_number)


#we must initialize guess and attempts, OR ELSE!!!!

attempts = 0
guess = None

#now for the game loopz. a WHile loop
while guess != secret_number and attempts <max_attempts:
    guess = int(input(f'Guess a number between 1 und {max_number}:   '))
    attempts += 1

    if guess < secret_number:
        print("Too low, @@")
    elif guess > secret_number:
        print('Too high, lul')
    else:
        print(f' Nice, Guess in {attempts} tries')
        break #dude, always remember to break!

#failed venture
if guess != secret_number:
    print(f' Out of tries QQ, Teh number was{secret_number}')         



