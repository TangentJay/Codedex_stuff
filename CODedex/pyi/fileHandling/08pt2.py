# CODedex/pyi/fileHandling/08pt2.py
'''
* Author: TanB
* Created: 8/6/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
"""Let's use .seek() and .truncate() to simulate unsending a message within a text file."""


snt_msg = 'Yo this es una secert msgg'
unsnt_msg = 'This secert has been unsent'

with open('snt_msg.txt' ,'w') as file:
    file.write(snt_msg)

with open('snt_msg.txt', 'r+') as file:
    ori_msg = file.read()
    file.seek(0)
    file.truncate(len(unsnt_msg))
    file.write(unsnt_msg)

print(f'original msg = {ori_msg} ')
print(f'unsent msg = {unsnt_msg}')