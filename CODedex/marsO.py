# Write code below 💖 6/12/2025  30
"""
Parameters and Arguments
So far, the functions we've created don't take in any input(s), 
which means they do the same thing each time they get called. A function can be far more useful than that!

Sometimes, we want our functions to perform a specific task, 
but the task varies depending on different input(s). And that's where parameters come in.

Parameters are just a fancy word for input. 
They are variables that a functions takes in. 
They go inside the parentheses in the function definition and are used inside the function.

For example, suppose we define and call a happy_birthday() function like so:
"""
def happy_birthday(): #
    print('happy birthday to you')
    print('happy birthday to you')
    print('happy birthday dear friend')
    print('happy birthday to you')
    
happy_birthday()

def happy_birthday(nombre):
    print('happy birthday to you')
    print('happy birthday to you')
    print('happy birthday dear '  + nombre)
    print('happy birthday to you')
happy_birthday('bill')