# CODedex/pyi/testing/caffee.py
'''
* Author: TanB
* Created: 8/18/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

class kaffeeMenu:
    def __init__(self):
        self.menu = {'black_kaffee': 3.69,
                     'koko': 2.70,
                     'dirt_wasser': 1.00,
                     'leche': 2.50
                     }
        

    def get_price(self, item):
        return self.menu.get(item.lower())
    

    def add_item(self, item, price):
        self.menu[item.lower()] = price