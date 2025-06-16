# Write code below 💖 6/14/2025 8 25 am  #35

#objects

"""
An object is an "instance" of a class. A class is simply a template for creating objects, 
which are individual copies of the class with actual values.

Using the Student class, let's create an object to model the iconic Wednesday Addams of Nevermore Academy – 
a boarding school for outcasts and misfits. The syntax for creating an object looks like this:

Wednesday Addams is a 11th-grade student with a 4.0 GPA and is currently enrolled. 🖤

You can check all the attributes available on the wednesday object with the built-in vars() function, as follows:


Now that we have created an object of Student and saved it to wednesday,
we can access and edit the class attributes by using the dot syntax, .attribute:
"""
#class x: # template for creating something
#object = an instance (real example) of un class
#_init_ method that sets up objects attributes
#self refers to the current object inside the class

#student class
class Student: #class
    student_id= 0  #class attributes / class variables
    name=''
    year=0
    gpa=0.0
    enrolled=False
   #object ⬇ 
wednesday=Student() # ⬆ using student class | now wednesday is an object or instance of student class
#wednesday is an instance of a class
wednesday.student_id =1113
wednesday.name = 'Wednsday Addams'
wednesday.year=11
wednesday.gpa=4.0
wednesday.enrolled=True


print(vars(wednesday))


# vars Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
