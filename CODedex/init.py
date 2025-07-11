# Write code below 💖 6/14/2025 10 05 am
# The __init__() Method

class Student:
    name=""
    year=0
    gpa=0.0
    enrolled=False
# the daniel object never received values from the Student class in the first place! We'd have to set them like so manually:
daniel=Student()

daniel.name= 'Daniel Li'
daniel.year = 10
daniel.gpa=4.0
daniel.enrolled=True

"""
Assigning a value to each attribute on a separate line is tedious; there must be an easier way! 
In fact, there is: we can use the __init__() method!

Using __init__() in our class definition lets us construct objects with unique attributes.
When we create a new Student() object, we can pass in values for each attribute to initialize the new object, all in a single line!

So if we reformat our Student class with __init__():
"""

print(vars(daniel))