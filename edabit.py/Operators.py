# Codedex_stuff/edabit.py/Operators.py
'''
* Author: TanB
* Created: 6/29/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#Types of Python Operators.
#Arithmetric
'''
print(5+7)#+ addition
print(5-7)#- subtraction
print(4*4)#multiplication
print(5/4)#division
print(5//4)# floor division
print(5%4)#modulo
print(6**2)#power 
#Assignment operator 
'''
#https://www.programiz.com/python-programming/keyword-list#and_or_not
o=9
t=8
o+=1 #addition assignment, o=o+1
o-=3# subtraction operator 0=0-3
o*=1#multiplication operator
o/=2#division operator o=o/0
o%=5#remainder operator o=o%5
o**=1#exponent assignment
print(o)
print(t)

#ex operator
f,y=8,9 # assign f any to 8 and 9
f+=y #f=f+b assign the sum of f+y to f
print(f)

# Comparison, operators compare two values 
print(4==5) #gives us false, is equall to
print(5!=6)#not equal to
print(6>7)#greater than 
print(6<7)#less than
print(6>=6) #greater than or equal to
print(2<=8)#less than equal to

 
# Logical, AND - OR - NOT
#a and b logical AND. TRUE if only both operands are TRUE
print(True and False) #Logical AND
print(True or False) #Logical OR
print(not False) #Logical NOT

# Bitwise, 
'''
Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
2 es 10 in binary, and 7 is 111
let x=10, 0000 1010 in binary, and y=4 0000 0100

l=10
m=4
print(l&m) #=0(0000 0000)
print(l|y)
print(l^m)
print(m>>2)
print(l<<m)
print()
'''

# Special, Idenity operators, is and is not are used to check  if two values are located at the same memory location
# it is importaint to note that having two variable with equal values dosen't necessarily mean they are identical
#  Identity operators in Python
x1=5
y1=5
x2='yoh'
y2='yoh'
x3=[1,2,3]
y3=[1,2,3]
print(x1,y1,x2,y2,x3,y3)
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

#Membership operators in python
message='sup world'
dict1={1:'a', 2:'b'}
print('s' in message) #checks if  s is the the messege
print('sup' not in message) #checks  if sup is present in messgge string
print(1 in dict1)# check if 1 key is present in dictionary1
print('a' in dict1) #checks if a keyis present in dict1. a is the value, 1 is the key