# Codedex_stuff/CODedex/pyi/Find_frends.py
# Write code below 💖

'''
* Author: TanB
* Created: 6/28/2025
* Company: Oosode

'''


#Tuples: Tuples are orderd collections that cannot be changed once created. Immutable
#Syntax. List and tuples have a few things in common: 
# They can store multiple items in a single vvriable. Their value are separated by commas
tuple_ex=(1,'2',True)
navy_blue=(0,0,128)
#Tuples are defined with/without  parenthese and their items can be a mixed of data type.
#  If there is only one item, make sure there is a comma , beside it
#valid tuple
t1=('a',)
t2='a',
#not a tuple
t3=('a')
#using tuples Tuples are also unpackable which allows you to easily turn them into variables.
#Most commonly, tuples are used as return values allowing you to easily work with large data sets.
full_name=('Ada', 'lovelace')
fn=full_name[0],[1]
#combine tuples
t4='a', 9
t5='b',
t6=t4+t5
print(t6)

My_Place=30,293312, -97.716742, 'Austin'
Friend_Place_1=17.321471, -0.655712, 'Mali '
Friend_Place_2=-37.697404, 175.045923, 'Auckland'
Friend_Place_3=51.389673,6.840046,'Essen'

Bonus= (My_Place+Friend_Place_1+Friend_Place_2+Friend_Place_3)
print(Bonus)