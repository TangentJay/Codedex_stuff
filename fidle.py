# Codedex_stuff/file.py
'''
* Author: TanB
* Created: 6/27/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#to import the os
'''
import os
print('working dic es: ', os.getcwd() )

file = open('fiv.txt', 'w+')  
# Opens (or creates) 'fiv.txt' for writing and reading.
# 'w+' mode: 
#   - If the file exists, it is cleared (emptied).
#   - If it doesn't exist, it is created.
#   - Allows both reading and writing.
python
Copy
Edit
file.write("Hello")  
# Writes the string "Hello" to the file.
# At this point, the file pointer is at the end of the written text.
python
Copy
Edit
file.seek(0)  
# Moves the file pointer back to the start (position 0).
# This is necessary before reading, because after writing, the pointer is at the end.
# Without seek(0), file.read() would return an empty string.
python
Copy
Edit
print(file.read())  
# Reads from the current file pointer (now at the beginning) to the end.
# Outputs: Hello
python
Copy
Edit
file.close()  
# Closes the file and ensures all changes are saved.
# Always a good practice to close files when done.

'''