# Push: Adds a new element on the stack.
# Pop: Removes and returns the top element from the stack.
# Peek: Returns the top (last) element on the stack.
# isEmpty: Checks if the stack is empty.
# Size: Finds the number of elements in the stack.

#stack is lifo | last in first out
bob = []
#push = .append
bob.append('yo')
bob.append('sup')
bob.append('datas')

print(f'bob new stack, {bob}')

#peek 
topelement = bob[-1]
print('peek:' , topelement)

#pop = .pop, removes
popb = bob.pop()
print(f'we dirty .pop {popb}')
print(f'stacked pop {bob}')

#is empty check if empty
isepmty =  not bool(bob)
print(f'es empty: {isepmty}')

#size of stack
print(f'size: {len(bob)}')

