# Write code below 💖 6/10/2025  #25

#List Methods
"""
Besides built-in functions, Python has a bunch of built-in list methods that are very handy.

Here are some of them:
.append() method adds an item to the end of the list.
.insert() method adds an item to a specific index.
.remove() method removes an item from a list based on the value.
.pop() method removes the item at a particular index.
Let's use DNA sequences as an example for this! 🧬
"""
dna =['AUG', 'AUC', 'UCG']

dna.append('UAA') 
dna.insert(2, 'GAU')
dna.remove('AUC')
dna.pop()
#dna.reverse()
dna.sort()
print(dna)

RL=['Harry Potter', "1984",'The Fault in Our Stars','The Mom Test', 'Life in Code']
RL.append("Pachinko")
RL.remove('The Fault in Our Stars')
RL.pop(1)
print(RL)

# passed ✔
"""
.append()	Add an item to the end of the list
.clear()	Remove all items from the list
.copy()	    Return a shallow copy of the list
.count()	Return the number of times the value appears in the list
.extend()	Appends another list to the current list by extending it
.index()	Returns the index of a value inside the list
.insert()	Insert an item at a specified position in the list
.pop()	    Remove an item from a specified position in the list
.remove()	Remove an item from the list based on the value of the item
.reverse()	Reverses the list in place
.sort()	    Sorts the list in place
"""