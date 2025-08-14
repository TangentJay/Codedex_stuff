# CODedex/pyi/fileHandling/15sornd.py
'''
* Author: TanB
* Created: 8/13/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

import random 

from functools import reduce


prefixes = ['John','Mystic','Dragon', 'Dark', 'Golden', 'Shadow', 'Sliver','Billy','CS']
suffixes = ['storm','Snow', 'fire', 'Lady', 'song', 'blade', 'whisper', 'bob' ,'50']


def create_fantasy_name(list1, list2):
    return random.choice(list1) + '' + random.choice(list2)


def capitalize_suffix(nombre): 

    return nombre.capitalize()


def BoB_name(nombre):

    return 'Bob' in nombre


def concat_names(name1, name2):

    return name1 + name2

#using map function to capitalize suffixes
capitalize_suffixes = list(map(capitalize_suffix, suffixes))

#list comprehension. Generating  x * names
random_names = [create_fantasy_name(prefixes, capitalize_suffixes) for _ in range(42)]

#filter bob in names
firaga_names = list(filter(BoB_name, random_names))

#reduce
reduced_name = reduce(concat_names, firaga_names, '')


def name_info():
    print('Some names you might love!: ')
    for name in random_names:
        print('-', name)

    print('\nBoB names: ')
    if firaga_names:
        for name in firaga_names:
            print('-', name)
    else:
        print('none found')

    print('\nreduced names: ')
    if reduced_name:
        print(reduced_name)

    else:
        ('N/A')


name_info()