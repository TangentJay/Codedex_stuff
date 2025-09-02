# projects2/myapp.py
'''
* Author: TanB
* Created: 8/22/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
''' 






todos = []
while True:
    user_action = input('Type add, show or q: ')
    match user_action:
        case 'add':
            todo_action = input('Enter a todo: ')
            print('Next')
            
            todos.append(todo_action)
        case 'show':
            print(todos)    
        case 'q':
            break
    
    

