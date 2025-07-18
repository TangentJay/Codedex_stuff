# CODedex/pyi/DSA/02DS.py
'''
* Author: TanB
* Created: 7/8/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

#List stores items in a specific order, allowing yoiu to add, remove and access items by their position(index)
cafe_menu =['Coffee', 'Espresso', 'Cappuccino', 'Latte']
breakfast_menu=['Coffee cake', 'Cinnamon roll',]
cafe_menu.append('Black tee')

print(cafe_menu[0:5])

#Dictionaries store key:values pairs . KEYS must be unique
book={'title': 'Bob goes to teh mall',
       'author': 'BillyBob',
        'genre': 'Fact', 'year': 2029 }

print(book['title'])

#sets store unique value sin an unorderd collection. {} curley brackets
setz={'Bob','Sun','MOOn','Oosode'}
setz.add('lemon')
print(setz)
print('lemon' in setz)

rpgz=['FFX','FFX-2','FFXI','FFXIII(1~3)','STar Ocean,TTEOT','Tales of symphonia','FFXII']

songz=[{'name': 'Enjoy teh silence', 'Artist': 'Depeche Mode', 'Year': 1990},
       {'name': 'ten album', 'artist': 'Pearl Jam', 'year': 1991}, 
       {'name': 'Flavour Trip', 'Artist': 'Many House mixes. Youtube', 'year': 'TBD'}]


places={'Abidjan','Cotonou', 'Freetown','Berlin','Leipzig','Dusseldorf' }

rpgz.append('Diablo 2(lod)')
print(rpgz)

songz.append({'name': 'Mr.Jones', 'Artist': 'Counting Crows', 'Year': 1993})
print(songz)

places.add('Novosibirsk')
print(places)