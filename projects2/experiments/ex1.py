# projects2/todo_app/experiments/ex1.py
'''
* Author: TanB
* Created: 8/21/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''



prompt = 'Enter a todo: '
print('Press Q or q to exit the program')



todos = []
while True:
    todo = input(prompt)
    print('Next')
    print(todo.title())
    todos.append(todo)
    
    if todo == 'q' or todo == 'quit':
        break


print(todos)