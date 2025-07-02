# Codedex_stuff/edabit.py/BasicIO.py
'''
* Author: TanB
* Created: 6/29/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#In Python we can simply use the print() function to print output
print('Python es awasome')

#syntax. in the above code, the print() function takes a single parameter,
# however, the actual syntax of the print function accepts 5 parameters
    #print(object= separator= end= file= flush=)
#object-value/s to be printed. 
#sep(separator) allows us to separate multiple objects inside print
#end-allows us to add specific values like new line '\n',tab '\t'
#file-where the value are printed. it's default value is sys.stdout
#flush-boolean specifying if the output is flushed or buffered. default: false

#ex1: print statement
print('Good morning')
print('it is rainy today')
'''
In the above example, the print() statement 
only includes the object to be printed. Here, the value for end is not used. Hence, it takes the default value '\n'.

So we get the output in two different lines.
'''

#Example 2: Python print() with end Parameter
print('good morning ', end='')#can add values to the output with end.
print('it is a rainy day')
'''
Notice that we have included the end= ' ' after the end of the first print() statement.

Hence, we get the output in a single line separated by space.
'''
#Example 3: Python print() with sep parameter
print('new year', 2026,'see u soon', sep=' t ' )#sep=controls characters or strings inserted betewwn multiple values

##output formatting
e,t=4,7

print('Teh value of e es: {} und t es: {}'.format(e,t))
print(f'and the same {e}  is teh {t}')#member to iunsert values

#python input
#using input to insert a number
num=input('enter un number: ')
print('u have entred ', num)
print('Data type of num: ',type(num))
'''
It is important to note that the entered value 10 is a string, not a number. 
So, type(num) returns <class 'str'>.
To convert user input into a number we can use int() or float() functions as:
'''
#num=int(input(stuff))

#dictionaries
#Dictionaries are unordered collections that allow you to store and access data with key:value parts
#single line
'''
dictionary={key:value}

#multi-line
dictionary={
key:value1,
key:value2,
key:value3,
}
The key:value pairs are comma-separated, surrounded by curly braces { }.

With lists and tuples, we access their items by index. But with dictionaries, we access their items by key. 🔑

'''

laptop={
'brand': 'Apple',
'model': 'Macbook Pro',
'size': 14,
'year': 2025
}
print(laptop)
#To access the value associated with a specific key in a dictionary, you use [ ] brackets with the key inside.
print(laptop['year'])

#creating a dicrionary
student_info={'name':'BoB', 'age' : 42, 'grade': 'C'}
#accessing dictionary elements
print('Name: ', student_info['name'] )
print('age ', student_info['age'])
print('grade: ', student_info['grade'])

#modify dictionary elements
student_info['age']=420
print('Modded age: ', student_info['age'])

#Dictionaries come equipped with various methods to streamline common tasks.
# This includes .keys(), .values(), and items():
print('Keys: ', student_info.keys())
print('Values: ', student_info.values())
print('Items: ', student_info.items())

