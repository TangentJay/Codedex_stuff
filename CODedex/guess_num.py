# Write code below 💖 1337

"""
 While Loop
Now that we got a sneak peek of a while loop, let's see what it does! 🔄

A while loop looks very similar to an if statement. Just like an if statement, 
it executes the code if the condition is True.

However, the difference is that the while loop will continue to execute the code inside of it,
over and over again, as long as the condition is True.
"""
tries = 0
guess = 0


while guess !=6 and tries < 5:
    guess = int(input('Guess teh number: '))
    tries = tries+1
    
if guess ==6:
    print('about time! ')
#elif guess !=6:
    #guess=guess+1
 #   print('again ')
else:
    print('nein')
#passed