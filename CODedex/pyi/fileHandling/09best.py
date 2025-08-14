# CODedex/pyi/fileHandling/09best.py
'''
* Author: TanB
* Created: 8/7/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#CSV
import os


import csv 

with open('tst1.csv', 'r', encoding='utf8') as file:

    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)

#------------------------------------ write to csv------------------------------------------

# data to write to csv file

dtw =[ ['name', 'age', 'grade'],
['jay',37, 'A'],
['bob', 42, 'B'],
['kim', 55, 'C'] ]

#open csv in write mode
with open('tst1.csv', 'w', newline='')as file:

    # create csv writer object
    csw = csv.writer(file)

    csw.writerows(dtw)
