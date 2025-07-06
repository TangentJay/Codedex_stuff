# Codedex_stuff/projects/quiz_game.py
'''
* Author: TanB
* Created: 7/4/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

#quiz game
print('Welcome to mi ??? quiz game')

playing=input('Do you want to play: ').lower() .strip()

if playing not in ['yes', 'y','ok', 'sure']: # alist
    quit()

print('Let\'s go! :)')
score=0#keeping track of teh score initilize

answer=input('What does CPU stands for? ').lower() .strip()
if answer == 'central processing unit':
    print('Correct')
    score+=1
else:
    #score-=1
    print('incorrect')

answer=input('What does GPU stands for ').lower() .strip()
if answer == 'graphical processing unit':
    print('Correct')
    score+=1 # score = score + 1
else:
    print('incorrect')
    #score-=1

answer=input('What does USB stands for? ').lower() .strip()
if answer == 'universal serial bus':
    print('Correct')
    score+=1
else:
    print('incorrect')
    #score-=1

answer=input('What is the name of the wire that allows you to connect to the internet? ').lower() .strip()
if answer in ['ethernet cable','cat5','cat6','cat7','cat8', 'lan cable']:
    print('Correct')
    score+=1
else:
    print('incorrect')
    #score-=1

print(f'You got {score} questions correct')
print(f'You got {score/4 * 100} %.')