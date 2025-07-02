# Codedex_stuff/CODedex/pyi/sets04.py
'''
* Author: TanB
* Created: 6/30/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#Sets
#sets are a collection of unique items with no duplicates.
#  They are unordered collections of distanct elements. 
# Each item in a set must be unique

#creating sets you can define sets by using curly brackets or the set() constructor, 
#each item is seperated by a comma


fruits={'apple','Banana','Orange'}

# Using sets: Sets support various methods that allow us to combine sets.
# find common items or filter out items. That make sets powerful for data manipulation

set1={1,2,3,4}
set2={3,4,5,6}

#union of sets
union_results=set1.union(set2)

#intersection of sets
intersection_results=set1.intersection(set2)

#differences of sets
difference_results=set1.difference(set2)
print(set1)
print(set2)
print(union_results)
print(intersection_results)
print(difference_results)
'''
.union(): Combines two or more sets and returns a new set.
.intersection(): Returns a set of items common to two or more sets.
.difference(): Returns a set of items found only in the calling set.
'''

#methods. There are more set methods for common operations, like adding and removing elements:
my_set={1,2,3}
my_set.add(4)
print(my_set)
my_set.remove(2)
print(my_set)
'''
The .add() method adds one new item to a set. If that item already exists, nothing happens.

The .remove() method removes an item from a set if it exists.
'''
mi_fruit={'Kiwi', 'Watermelon','Lychee','Fig','Lemon','Plum'}
Friend_fruit={'Banana','coconut','Grape','Melon','Fig','Kiwi'}

union_fruit=mi_fruit.union(Friend_fruit)
intersection_fruit=mi_fruit.intersection(Friend_fruit)
diff_fruit=mi_fruit.difference(Friend_fruit)

print(mi_fruit)
print(Friend_fruit)

print(union_fruit)
print(intersection_fruit)
print(diff_fruit)