# Codedex_stuff/CODedex/pyi/o7_fileRealm.py
'''
* Author: TanB
* Created: 7/4/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

#opening files. when handling files, du have to open it first.
# we use the open() function

#file=open(file_path, mode)
#the open() function takes to arguments:


file=open('Diaries.txt' ,'r')

#content=file.read()

#print('Using read(): ')
#print(content)

line1=file.readline() #reads teh first line
print(line1,end='')

line2=file.readline()# reads the second line
print(line2)

l3=file.readline()
print(l3)

l4=file.readline()
print(l4)
file.close()