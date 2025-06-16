# Write code below 💖 6/14/2025 15 39 #36


"""
Ever wonder how many people live in New York City? What about London?

Create a favorite_cities.py program.

Let's make a City class that uses the __init__() method to define the following attributes:

name (string)
country (string)
population (integer rounded to the nearest thousand people)
landmarks (list of strings)
Next, create an object for your hometown and assign the attributes above.

Lastly, create another object for the city that you've always wanted to visit!


"""

class Favorite_city:
    def __init__(self,name,country,population,landmarks, Boss, Code_name):
        self.name=name
        self.country=country
        self.population=population
        self.landmarks=landmarks
        self.Boss=Boss 
        self.Code_name=Code_name 
konohagakure=Favorite_city('konohagakure', 'Konoha', 1337420, ['Hokage Rock', 'Elder shrine'],'Naruto', 'Hidden Leaf')
Amegakure=Favorite_city('Amegakure','unnamed',42069, ['Pain tower', 'Nagato shrine'],'Pain','Hidden Rain' )

print(vars(konohagakure))
print(vars(Amegakure))

#passed ✔