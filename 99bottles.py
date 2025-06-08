# Write code below 💖

"""
Electronic Delay Storage Automatic Calculator (EDSAC)

String Interpolation
Let's learn a new tool that's very similar to string concatenation, before continuing on to the instructions.

String interpolation is a process of substituting values of variables into placeholders in a string.

For instance, if you have a template for saying hello to a person in an email like 'Hi {name}, 
nice to meet you!', you would like to replace the placeholder {name} with an actual name.
This is string interpolation.

The above program can be recreated using string interpolation using the {} sign:
"""

# String concatenation 
#for i in range(2):
  #  print('the square of ' + str(i) + ' es ' + str(i*i))
    
# String Interpolation . fstrings? {} 

#for i in range(3):
 #   print(f'The square of {i} ist {i*i}')
    
    
# range (x,y,z) start, stop and steps 

for i in range(99,0,-1):
   if i >1:
    print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
    print(f'Take one down, pass it around, {i-1} bottles of beer on the wall. \n') 
   else:
       print('1 bottle of bier on the wall, 1 bottle of bier.')
       print('Take one down, pass it around, no more bottles of bier on teh wall. \n')

#passed