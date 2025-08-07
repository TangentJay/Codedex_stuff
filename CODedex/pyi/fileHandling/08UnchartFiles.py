# CODedex/pyi/fileHandling/08UnchartFiles.py
'''
* Author: TanB
* Created: 8/6/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
fp = 'Ello.txt'




# try:
#     file = open(fp, 'r')
#     #file.write('\n8,6,2025 stuff|  19:54\n')
#     file.read()
# finally:
#     file.close()


with open('Ello.txt','r') as file:
     file.seek(2)
     re = file.read()
     print(re)

# with open('Ello.txt', 'r') as file:
#     file.seek(10)
#     f = file.read
#     print(f)

'''The .truncate() method allows us to modify file size. 
This is useful when we want to remove or reset content beyond a certain point.
 We can trim or extend the file size as needed.

# Truncating a file
with open('example.txt', 'a') as file:
file.truncate(20)  # Limit the file size to 20 bytes'''

