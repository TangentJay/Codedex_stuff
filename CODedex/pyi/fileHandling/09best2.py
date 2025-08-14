# CODedex/pyi/fileHandling/09best2.py
'''
* Author: TanB
* Created: 8/7/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import csv

with open('bs1.csv','r', encoding='utf8') as file:
    cr = csv.reader(file)

    for row in cr:
        print(row)



for row in cr:
    current_sales = float(row[4])

    if current_sales > max_sales:
        max_sales = current_sales
        best_selling_book = row



# with open('bsi.csv', 'w', newline='') as file:
#     csvW = csv.writer(file)

