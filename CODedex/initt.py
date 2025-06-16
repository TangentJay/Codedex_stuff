# Write code below 💖 6/14/2025 15 28  #36
# The __init__() Method

class Student: #class/blueprint
    name=""
    year=0
    gpa=0.0
    enrolled=False
# the daniel object never received values from the Student class in the first place! We'd have to set them like so manually:
daniel=Student() #object/instance =daniel in this case

daniel.name= 'Daniel Li'
daniel.year = 10
daniel.gpa=4.0
daniel.enrolled=False
print(vars(daniel))
"""
Assigning a value to each attribute on a separate line is tedious; there must be an easier way! 
In fact, there is: we can use the __init__() method!

Using __init__() in our class definition lets us construct objects with unique attributes.
When we create a new Student() object, we can pass in values for each attribute to initialize the new object, all in a single line!

So if we reformat our Student class with __init__():
"""
#tst
class Student:
    def __init__(self, name, year,gpa, enrolled):
        self.name=name
        self.year=year
        self.gpa=gpa
        self.enrolled=enrolled
        
daniel=Student('Daniel Li', 10, 4.0,True)
ladybird=Student('Christine McPherson',12,4.0,True)
kyle= Student('Kyle Scheible',12, 3.4, True)


print(vars(ladybird))
print(vars(daniel))
print(vars(kyle))        
        







"""
Note that __init__() also uses a separate parameter called self. 
This represents the object we'll create out of Student(). 
We need to include self whenever we want to use __init__(). It's always the first parameter.

With self, we can move each of the previous assignments, 
like daniel.name = 'Daniel Li', into the method and slightly rewrite it, like self.name = name.

Creating objects is now so much easier!
If we want to create two more objects based on characters in Lady Bird, we just have to write:
"""        