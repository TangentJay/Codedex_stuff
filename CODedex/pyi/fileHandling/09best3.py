# CODedex/pyi/fileHandling/09best3.py
'''
* Author: TanB
* Created: 8/8/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import csv

cr = 'bs1.csv'

with open('bs1.csv', 'r', encoding='utf8') as file:
    cr = csv.reader(file)

    next(cr)
    maxSales = 0
    best_sellingb = None

    for row in cr:
        current_sales = float(row[4])
        if current_sales > maxSales:
            maxSales = current_sales
            best_sellingb = row

with open('bsi.csv','w', newline='') as file:
    csvW = csv.writer(file)
    csvW.writerow(best_sellingb)

print(row)
print(f'Teh best selling bookz sind:{best_sellingb}')