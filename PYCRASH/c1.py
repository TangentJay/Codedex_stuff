#6/10/2025 zzz  mush
#Error types
#Syntax Errors
#Runtime errors
#Logic errors

"""
Syntax Errors
The syntax is a set of guidelines that needs to be 
followed in order to write correctly in a computer language.
A syntax error is a missing punctuation character, 
a mistake such as a misspelled keyword, 
or a missing closing bracket. 
The syntax errors are detected by the compiler or the interpreter. 
If you try to execute a Python program that contains a syntax error, you will get an error message on your screen and the program won't execute. 
You must correct any errors and then try to execute the program again. 
Usually these types of errors are due to typos. In case an error occur the Python interpreter stops running.
Some commons causes of syntax errors are due to:
Wrongly written keywords
Wrong use of an operator
Forgetting parentheses in a function call
Not putting strings in single quotes or double quotes

Runtime Errors
These errors occur when the execution of the code is stopped because of an operation being impossible to be carried out.
A runtime error can cause a program to end abruptly or even cause system shut-down. Such errors can be the most difficult errors to detect.
Running out of memory or a division by zero are examples of runtime errors.

Logical Errors
Logical errors happen when the code produces wrong results. For instance a temperature conversion from Fahrenheit to Celsius
"""

print("20 degree fahrenheit in degree cel es: ")
#print(5/9 *20-32) #error logic  error
#print (5/9 * (20-32) ) ✔

# logic errors gives no warning
#print('I'm good' ) #SyntaxError: unterminated string literal

#month=['jan','feb','mar','apr','may'] #blist
#print(month)

name="BoB"
lname="bill"
age=1337
weight=420
height=69
job="stuff"
#print(name age height job)#syn error
#print(name, age, height, job) ✔
print(job + lname) #string object | ConCateNate  ~ oh hi Nate!
# since this is Python we are dealing with, everything within this language is considered as an object, thus the Object-Oriented Programming nature.
# I can also str() in a variable 
#txt2=str(4)
#f stringz | formatted {}. member, f before""
n1=input("tu nombre: ")
a1=int(input("How old are you: "))
city=input('where do you live? ')
eMale=input("What es dein email add: ")



print(f'Hello {n1} und welcome to my interactive sercives! I will contact u @{eMale}.')
