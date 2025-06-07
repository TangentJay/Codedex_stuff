# Write code below 💖

slytherin=0
ravenclaw=0
gryffindor=0
hufflepuff=0

print('Tres preguntas ich will ask which will decide dein faith! ' )

print('Qestion eins: Do you like Dawn or Dusk? \n1)Dawn \n2)Dusk ')
ans=int(input('1 oder 2: '))
if ans ==1:
    gryffindor=gryffindor+1
    ravenclaw=ravenclaw+1
elif ans ==2:
    hufflepuff=hufflepuff+1
    slytherin=slytherin+1
else:
    print('error')
print("When I'm ded, I want people to remember me as: \n1)The Good \n2)The Great \n3)The WIse \n4)The Bold \n")
ans=int(input('1 ore 4: '))

if ans ==1:
    hufflepuff=hufflepuff+2
    print('+2 to Hufflepuff')
elif ans ==2:
    slytherin=slytherin+2
    print('+2 to SLytherin')
elif ans ==3:
    ravenclaw=ravenclaw+2
    print('+2 Ravenclaw')
elif ans ==4:
    gryffindor=gryffindor+2
    print('+2 to Gryffindor')
else:
    print('Wrong input')

print("Which kind of instrument most pleases dein ear?  \n1)The violin \n)2The trumpet \n3)The piano \n4) The drum \n ")
ans=int(input("1 are 4: "))
if ans ==1:
    slytherin=slytherin+4
    print('+4 Slytherin')
elif ans ==2:
    hufflepuff=hufflepuff+4
    print('+4 Hufflepuff')
elif ans ==3:
    ravenclaw=ravenclaw+4
    print('+4 Ravenclaw')
elif ans ==4:
    gryffindor=gryffindor+4
    print('+4 Gryffindor')
else:
    print(' Wrong input')

print(f'slytherin has: {slytherin} points, \nravenclaw has: {ravenclaw} points, \ngryffindor has: {gryffindor} points, \nhufflepuff has: {hufflepuff} points.')



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
