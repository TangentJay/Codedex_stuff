# CODedex/pyi/fileHandling/07Filereals.py
'''
* Author: TanB
* Created: 7/26/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#opening files

# file = open(file_path, mode)
"""The open() function takes two arguments:

The file_path, such as 'filename.txt'.
The mode for how to use the file.
r, reading a file
w, writing to a file
a, append| writing to the end of the file

You can write to a file with various methods. The write() method simply writes data to a file:

file.write('text')
"""

bob2 = open('Ello2.txt', 'w')

bob2.write('Round dos, here we go.\n')
bob2.write('7/26/2025, come on man \n')

# You can also write multiple lines to a file at once with the writelines() method:
lines = ['Just writing multiple lines\n', 'Using the writelines() method\n']
bob2.writelines(lines)
#The writelines() method takes a list of lines and writes them to the file.

#reading files

"""The .read() method lets you read the entire content of a file. 
This method can be saved to a variable and printed to the terminal:"""

bob2 = open('Ello2.txt', 'r')
stuff = bob2.read()
#print(stuff)

"""The .readline() method lets you read a file one line at a time:"""

for line in stuff:
    print(line, end='')
print(bob2)
bob2.close()

with open('Ello.txt', 'r') as b:
    print(b.read())

