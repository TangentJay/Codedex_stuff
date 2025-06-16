# Write code below 💖 6/14/2025 zzz  4 33 aam

"""
Congrats!
Congratulations! You now know how functions work. ***
This is a concept that trips up a lot of people, so definitely practice and practice. 💪

In this chapter, we learned:

The "Don't Repeat Yourself" methodology.
We've been using built-in functions like print() and input() all along.
How to define and call a function — the two-step process.
Inputs with parameters and arguments.   def fun(PARAMETER <-X)
Outputs with the return keyword.
Function scope vs. global scope.
Here's the function skeleton one more time, just in case you forget!

DEF FUNCTION_NAME(PARMETER1, PARAMETER2):
    # SOME CODE
   RETURN VALUE
"""
"""
When you go to a drive-thru like McDonald's, you can order food using the item numbers. For example, a Happy Meal might be a #3!

Create a drive_thru.py program with your favorite fast food chain's menu.

Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!

For example, if you called the function with:

Argument value 1, it could return '🍔 Cheeseburger'.
Argument value 2, it could return '🍟 Fries'.
Argument value 3, it could return '🥤 Soda'.
Argument value 4, it could return '🍦 Ice Cream'.
Argument value 5, it could return '🍪 Cookie'.
Make sure to call this function a few times to make sure that it works!

Lastly, let's do the following:

Create a welcome menu and put that in a welcome() function.
Create a main program that takes in user input with input().
"""
def get_item(O):
    if O==1:
        return '🌭 Hotdog'
    elif O==2:
        return'🍚 Rice'
    elif O==3:
        return '🍬🌽 Candycorn'
    elif O==4:
        return '🥕 Karrot'
    elif O==5:
        return '🍞 Bort'
    elif O==6:
        return '🍦 Ice Cream'
    else:
        return'Option not on menu'
    
def noms():
    print('Hi This es mein place of noms to consume for energy or so! Take a look: ')
    print('1) 🌭 Hotdog')
    print('2) 🍚 Rice')
    print('3) 🍬🌽 Candycorn')
    print('4) 🥕 Karrot')
    print('5) 🍞 Bort')
    print('6) 🍦 Ice Cream')
    
noms()

pick= int(input('Select dein order: '))
print('Here is your stuff:',  get_item(pick))


#passed ✔