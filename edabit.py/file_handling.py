# Codedex_stuff/file_handling.py
'''
* Author: TanB
* Created: 6/27/2025 13:41
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#Create a file using python script
#you can give any name to the variable, but we will call it file for now
#using the open function, you can give any name to the parameter and use the correct extention

file=open('fiv.txt','w+') 
#after the , comma you must enter a mode, 
# there are 4 or five modes,'R' read,'W' write,'A' append , exclusive creation'X'
'''
Mode
Description

‘r’	Open text file for reading. Raises an I/O error if the file does not exist.
‘r+’	Open the file for reading and writing. Raises an I/O error if the file does not exist.
‘w’	Open the file for writing. Truncates the file if it already exists. Creates a new file if it does not exist.
‘w+’	Open the file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist.
‘a’	Open the file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
‘a+’	Open the file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
‘rb’	Open the file for reading in binary format. Raises an I/O error if the file does not exist.
‘rb+’	Open the file for reading and writing in binary format. Raises an I/O error if the file does not exist.
‘wb’	Open the file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
‘wb+’	Open the file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
‘ab’	Open the file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
‘ab+’	Open the file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
'''

