# Write code below 💖 6/14/2025 5 17 am  #34


"""
Classes
As technologists, we create programs to solve problems that stem from everyday life. 
In the real world, the objects around us are complex.

Suppose we want to build a database of students in a school,
where each student has different attributes, like name, year, GPA, and enrollment status.

Using our previous knowledge, we could represent each student as a list:

# Lists with student id, name, year, gpa, and enrolled status

student_1 = [1001, 'Asiqur', 10, 3.7, True]
student_2 = [1002, 'Jerry', 9, 3.8, True]
student_3 = [1003, 'Rose', 12, 3.6, False]

However, we have no way of knowing which item corresponds to which attribute – it will get messy fast. 
For example, does student_2[1] refer to the name, year, or GPA?

This is where classes come in!

With classes, we can create our own data types and use them to model everyday objects with unique characteristics and behaviors.

Classes serve as a template for the objects created using that class. Simply put, 
a class is like a blueprint. It can make a bunch of objects with identical sets of attributes,
similar to how a car manufacturer can use a model blueprint to build hundreds of cars with different colors, interiors, wheels, etc.

In our example, 📜 (class) ➡️ 👩🏼‍💻👨🏻‍💻👩🏽‍💻👩‍💻🧑🏾‍💻 (objects).

Here's the basic syntax for creating a class in Python:
The class keyword followed by class name creates the class. By convention, the class name is capitalized.

For example, to make a Student class, we can write:

class Student:
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False

The Student class has four attributes:

.name of the type str (text string)
.year of the type int (integer number)
.gpa of the type float (decimal number)
.enrolled of the type bool (boolean value)
With this class, we can represent each class attribute as a variable, 
and we will learn how to access or change them in later sections! For now, let's implement a class.

list with student- id, name, year, gpa and enrolled status

student_1=[1001, 'Asiqur', 10 ,3.7 ,True]
student_2=[1002, 'Jerry', 9, 3.8, True]
Student_3=[1003, 'ROse', 12, 3.6, False]

print(student_2[1])
"""