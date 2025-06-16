# Write code below 💖 6/14/2025 9 40 am  #35


#class x: # template for creating something
#object = an instance (real example) of un class
#_init_ method that sets up objects attributes
#self refers to the current object inside the class
"""
In the last exercise, we created a Restaurant class.

In a new file called bobs_burgers.py, 
create an instance of the Restaurant class called bobs_burgers with the following attributes:

'Bob\'s Burgers'
'American Diner'
4.7
False
Once you do that, 
create two more instances of the Restaurant class with your favorite dinner spots nearby.

Then, use print(vars()) to output each of the three restaurants!
"""



class Restaurant:
    name=''
    category=''
    rating=0.0
    delivery=True
    
    
bobs_burger= Restaurant()
bobs_burger.name="Bob's Burgers"
bobs_burger.category ='American Diner'
bobs_burger.rating = 4.7
bobs_burger.delivery = False


Oosode_kaffee=Restaurant()
Oosode_kaffee.name="Oosode's kaffee"
Oosode_kaffee.category='Coffee and stuff'
Oosode_kaffee.rating= 1337
Oosode_kaffee.delivery= True





print(vars(Oosode_kaffee))
print(vars(bobs_burger))

#passed ✔