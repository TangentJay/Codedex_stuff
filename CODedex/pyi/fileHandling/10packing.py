# CODedex/pyi/fileHandling/10packing.py
'''
* Author: TanB
* Created: 8/8/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

import csv

data = [['Itemz', 'Quantity'], ['blender', 2], ['posterz', 10],
        ['shoez', 4]]

try:
    with open('pack.csv', 'r', encoding='utf-8', newline='') as file:
        cvr = csv.reader(file)
        for row in cvr:
            print(row)


except FileNotFoundError:
    print('error, no list....creating new list')
    with open('pack.csv', 'w', encoding='utf-8', newline='') as op:
        cvw = csv.writer(op)
        cvw.writerows(data)
    print('packing file created')

