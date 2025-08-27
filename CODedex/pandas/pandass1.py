# CODedex/pandas/pandass1.py
'''
* Author: TanB
* Created: 8/19/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import pandas as pd

data = { 'OS': ['Windows', 'Mac', 'Linux'],
        'usage':['Gaming', 'legscross','manmode' ],
         'price': ['affordable', 'armNleg', 'free'] }

df = pd.DataFrame(data)

print(df)

dataa = [['Mr\'Jones', 'US', 1337420], ['Mate_jr', 'AUS', 4445678],  ['BobbieBoi', 'USA', 8567342], ['RAM', 'MotherBoard', 1100110]]

dff = pd.DataFrame(dataa, columns=['city', 'country','population'])


print(dff)