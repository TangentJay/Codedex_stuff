# Codedex_stuff/edabit.py/D3.py
'''
* Author: TanB
* Created: 6/27/2025  12:33
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#Match statement is used to perform different actions based on different conditions
#Instead of writing many if..else statements, you can match statement. 
# The match statement selects one of many code blocks to eb executed

day=4 
match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('Not Today: Thursday')
    case 5:
        print('Friday')
    case 6:
        print(' Saturday')
    case 7:
        print('Sunday')   

#combine values. use the pipe(|) 
# character as an or operator in the case evaluation to check for more than one value match in one case:
match day: 
    case 1|2|3|4|5:
        print('Today es a weekday')
    case 6|7:
        print('I love weekends!') 

#if statement as Gaurds. 
# You can add if statement in the case evaluation as an extra condition-check:              
month=4
match day:
    case 1|2|3|4|5 if month==4:
        print('A weekday in April')
    case 1|2|3|4|5 if month==5:
        print('A weekday en May')    
    case _:
        print('No match')