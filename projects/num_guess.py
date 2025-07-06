# Codedex_stuff/projects/num_guess.py
'''
* Author: TanB
* Created: 7/5/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''


import random
#random.randint(1,10) includes 10. no upper bound
#random.randrange(start,stop)

top_of_range=input('type a number: ')

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range <= 0:
        print('Please type a number larger than zero next time')
        quit()
else:
    print('Please type a number next time ')
    quit()



ran = random.randint(0,top_of_range)#10 es upper bound. will generate upp to 9. Member to include
guesses=0

while True:
    guesses+=1
    user_guess = input('Make a guess: ')
    if user_guess .isdigit():
        user_guess = int(user_guess)

    else:
        print('Please type a number next time')
        continue# a loop

    if user_guess == ran:
        print(f'BingoO! Teh number was {ran}') 
        break  
    elif user_guess > ran:
       print('Try agen! Too high')
    else:
        print('You are below teh number!')   
        
        

        





print(f'You got it in {guesses} guesses')