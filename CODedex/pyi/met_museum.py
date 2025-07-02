# Codedex_stuff/CODedex/pyi/met_museum.py
'''
* Author: TanB
* Created: 6/29/2025
* Company: Oosode
'''
#dictionaries
#Dictionaries are unordered collections that allow you to store and access data with key:value parts
#single line
'''
dictionary={key:value}

#multi-line
dictionary={
key:value1,
key:value2,
key:value3,
}
The key:value pairs are comma-separated, surrounded by curly braces { }.

With lists and tuples, we access their items by index. But with dictionaries, we access their items by key. 🔑

'''

laptop={
'brand': 'Apple',
'model': 'Macbook Pro',
'size': 14,
'year': 2025
}
print(laptop)
#To access the value associated with a specific key in a dictionary, you use [ ] brackets with the key inside.
print(laptop['year'])

#creating a dicrionary
student_info={'name':'BoB', 'age' : 42, 'grade': 'C'}
#accessing dictionary elements
print('Name: ', student_info['name'] )
print('age ', student_info['age'])
print('grade: ', student_info['grade'])

#modify dictionary elements
student_info['age']=420
print('Modded age: ', student_info['age'])

#Dictionaries come equipped with various methods to streamline common tasks.
# This includes .keys(), .values(), and items():
print('Keys: ', student_info.keys())
print('Values: ', student_info.values())
print('Items: ', student_info.items())
'''
.keys() returns just the keys from a dictionary.
.values() returns just the values.
.items() returns a list of the key-value pairs as tuples.
'''

'''
Met_Art1={'artist': 'Tairona artists', 'period':  'Tairona', 'date' : '900-1699 CE',  }
Met_Art2={'artist': 'South central Veracruz artists', 'period': 'Classic Veracruz', 'date': '600-1000 CE',  }
Met_Art3={'artist': 'Maya artists', 'period': 'Maya', 'date': '410-650 CE',}  
print(Met_Art1, Met_Art1.keys(),Met_Art1.values())
print(Met_Art2, Met_Art2.keys(),Met_Art2.values())
print(Met_Art3, Met_Art3.keys(), Met_Art3.values())
'''


# Write code below 💖

Figure_pendant={'artist': 'Tairona artists', 'period':  'Tairona', 'date' : '900-1699 CE',  }
Smiling_figure_Sonriente={'artist': 'South central Veracruz artists', 'period': 'Classic Veracruz', 'date': '600-1000 CE',  }
Mirror_bearer={'artist': 'Maya artists', 'period': 'Maya', 'date': '410-650 CE',}  
print(Figure_pendant, Figure_pendant.keys(),Figure_pendant.values())
print(Smiling_figure_Sonriente, Smiling_figure_Sonriente.keys(),Smiling_figure_Sonriente.values())
print(Mirror_bearer, Mirror_bearer.keys(), Mirror_bearer.values())