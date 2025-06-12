# Write code below 💖6/12/2025
#https://docs.python.org/3/library/functions.html
# Define a Function
"""
To define a function, we need a function definition. A function definition begins with the def keyword, 
followed by the function name, a set of parentheses, and a colon, in that order.The def keyword.
The function name, followed by a pair of parentheses ().
The colon :.
The code inside the function is called the body of the function. 
And just like if statements and while loops, the code inside a function must be indented.

Note: The common naming convention for functions is snake_case.

Suppose we want to create a function named say_hello():
 Call a Function
To call a function, we use the function name followed by parentheses somewhere in the code:

 Fortune Cookie is a small cookie wafer with a piece of paper inside, called a “fortune”, which is usually a Chinese phrase with translation and a list of lucky numbers. They are served in restaurants in the U.S. and Canada. 🥠

Create a fortune_cookie.py program that gives the user random fortunes.

Define a function named fortune(). Inside the function, print out a random fortune from the list of options below:
"""

#def say_hello():
 #   print('Ello! ')
   #  print('How are U? ')

#say_hello()

#for i in range(3):
 #   print(say_hello())
 
import random
#-
def fortune():
    random_fortune=random.randint(0,7)
    if random_fortune == 0:
        return "Don't pursue happiness - create it."
    elif random_fortune == 1:
        return'All things are difficult before they are ez'
    elif random_fortune ==  2:
        return'*The early bird gets the worm, but the second mouse gets the cheese'
    elif random_fortune == 3:
        return'Someone in dein life needs a letter from you.'
    elif random_fortune == 4:    
        return"Don't just think. Act!"
    elif random_fortune ==5:    
        return'Your heart will skip a beat.'
    elif random_fortune ==6:    
        return'The fortune kookie tu search for es en another cookie'
    #elif random_fortune ==7:    
     #   return"Elp! I'm being held prisoner in a Chinese bakery!"
    else:
        return"Elp! I'm being held prisoner in a Chinese bakery!"

print(fortune()) # understand difference later
print(fortune())
print(fortune())
#GG