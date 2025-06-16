# Write code below 💖 6/15/2025 2 04 am  #37

"""
 Instance Methods
Now that we can create classes and objects, and edit their properties, our last step is to create functions.

Wait... functions in classes?! Isn't that super complicated?

Actually, it's not. Functions that are defined in a class are called methods. In fact, we have already used a bunch of methods. For example, in exercise 25, we looked at a few built-in list methods, such as:

.insert()
.append()
.remove()
These are built-in methods. Let's create our own methods within a class!
"""

class Student:
    def __init__(self, name, year, enrolled, gpa):
        self.name=name
        self.year=year
        self.enrolled=enrolled
        self.gpa=gpa
    
    def display_info(self):
        print('The student ' + self.name + "\'s GPA is " + str(self.gpa) + '!')
    
    def graduation(self):
        if self.enrolled and self.gpa > 2.5 and self.year==12:
         print(self.name + ' will be able to graduate this year!')    
        
mitsuha = Student('宮水三葉', 11,False, 4.0)
taki=Student('立花瀧', 11, True, 3.8)

mitsuha.display_info()
taki.display_info()

# *taki.graduation()
"""
To implement a method, we need to define one inside the class. 
For example, if we want to create a method called .display_info(), we would define it like so:
"""

