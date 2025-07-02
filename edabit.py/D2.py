# Codedex_stuff/edabit.py/D2.py
'''
* Author: TanB
* Created: 6/26/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#Let's create a variable from scratch
'''
Declare the variable 'food'
Assign the variable food the value 'pizza'
'''
food='pizza'

day=19 #if a number does not contain a decimal , it;s an interger

division=100/2

#Use the + operator to concatenate(combine) two strings together
fn='luke '
ln='skywalker'

name=fn + ln
print(name)

#define/functon are block of code  that can be named and reused. RETURN
#basic function 
def add_two_numbers(num1,num2):# add_two_numbers is the name of the function, num1 and num2 are the parameters()
    return num1 + num2 # return is teh keyword that exits the function and return a vlue(output)
print(add_two_numbers(5,6))
#although functions usually take parameters, they dont necessarily have to
def h():
    return 'Hello World!'

print(h())
 
 #list. are list of tiems.Pythons list are functionally similar to arrays in other languaes
fruit=['apple', 'banana','orange', 'mango', 'tomato']
#each fruin in the above  list is called an element. list elements can be any value
stuff=[True, 1976, None,'yoh']
#each element in a list has an index that starts at 0
#to access a specific element within a list, we do this:
fruit[2]
print(fruit+stuff)

#return 'Donatello' Member thee first element in a list es 0. lways return your answer
turtles=['Raphael', 'Michelangelo','Leonardo','Donatello']
def turtle_power(turtles):
    return turtles [2]
     
#print(turtle_power(turtles[3]))
print(turtle_power(turtles))

#Mutable element in a list means they can be changed
numbers=[14,56,78]
#to change the value of 14 (at index 0)we do this:
numbers[0]=35
print (numbers)
#given a list of numbers, set the value of data stored at index 1 to 88
numberz=[1,4,6,8,0]
numberz[1]=88
print(numberz)
#len() in most cases you wn't know the excat length of a list.
# in other words, you wont know how many elements it counts.
# that's where the .length() function comes in
movies=['The Matrix','Se7en','The wizard of oz', 'Mary poppins']
#to get the excat length of movies list, we would use len() function
len(movies)
print(len(movies))
#gives the list lst of unknown length, return its length
def get_length(lst): #function defition
    return len(lst)

print(get_length([4,5,7,2,4,'shame'])) #function call. The arguments is 4,5,7,2,4,'shame'
#the argument is assigned to the parameter lst during the function call.
# Then inside the function, lst behaves like a regular variable that equals[1,2,3]

#Think of a function as a blender and the parameter is the ingredient placeholder
def blend(ingredient):
    return 'blended ' + ingredient
print(blend('green_grapes'))

#dictionaries. Dictionires are eaiser to store and maintain information, like this:
person1={'first_name': 'Joffery',
         'last_name':  'Baratheon',
         'email': 'joff@omail.com'}
person2={'first_name':'Jon',
        'last_name': 'Snow',
        'email': 'jonsnowz@mymail.com'}
person3={'first_name': 'Billy',
         'last_name': 'bob',
         'email': 'bobbie@xmail.com'}

person4 = {'first_name': 'Daenerys',
'last_name': 'Targaryen',
'email': 'dragonlady@gmail.com'
  
}

#the things on the left of : are called keys and the things on the righjt are the values. 
# We refre to them as key-values pairs

print(person4)
#finish 22:09