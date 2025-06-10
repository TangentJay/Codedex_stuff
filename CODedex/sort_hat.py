# Write code below 💖
"""
Here's a recap of everything we learned so far:

Control flow is the order in which the program's code executes.
if statement tests a condition for truth and executes the code if it's True.
elif clause can be added between if and else.
else executes the code if none of the above is True.
Relational operators are used to compare two values: ==, !=, >, >=, <, <=.
Logical operators are used to combine two or more conditions: and, or, not.
Here's an if/elif/else statement in action just in case:


The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry.
The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin
Write a program that asks the user some questions with the int() and input() functions:
"""

slytherin=0
ravenclaw=0
gryffindor=0
hufflepuff=0

print('Tres preguntas ich will ask which will decide dein faith! ' )
print('Please pick a number')
Q1=int(input("Do you like Dawn or Dusk? \n1)Dawn \n2)Dusk \n "))

if Q1 ==1:
    gryffindor=gryffindor+1
    ravenclaw=ravenclaw+1
    print(" +1 to Gyffindor and Ravenclaw ")
elif Q1 ==2:
    hufflepuff=hufflepuff+1
    slytherin=slytherin+1
    print(' +1 to Hufflepuff and Slytherin')
else:
    print('error')


Q2=int(input("When I'm ded, I want people to remember me as:  \n1)The Good \n)2The Great \n3)The WIse \n4)The Bold \n"))

if Q2 ==1:
    hufflepuff=hufflepuff+2
    print('+2 to Hufflepuff')
elif Q2 ==2:
    slytherin=slytherin+2
    print('+2 to SLytherin')
elif Q2 ==3:
    ravenclaw=ravenclaw+2
    print('+2 Ravenclaw')
elif Q2 ==4:
    gryffindor=gryffindor+2
    print('+2 to Gryffindor')
else:
    print('Wrong input')


Q3=int(input("Which kind of instrument most pleases dein ear?  \n1)The violin \n)2The trumpet \n3)The piano \n4) The drum \n "))
if Q3 ==1:
    slytherin=slytherin+4
    print('+4 Slytherin')
elif Q3 ==2:
    hufflepuff=hufflepuff+4
    print('+4 Hufflepuff')
elif Q3 ==3:
    ravenclaw=ravenclaw+4
    print('+4 Ravenclaw')
elif Q3 ==4:
    gryffindor=gryffindor+4
    print('+4 Gryffindor')
else:
    print(' Wrong input')

print(Q1)
print(Q2)
print(Q3)

print(f'slytherin has: {slytherin} points, \nravenclaw has: {ravenclaw} points, \ngryffindor has: {gryffindor} points, \nhufflepuff has: {hufflepuff} points.')
