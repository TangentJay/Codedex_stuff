# Cryptostuff.py
'''
* Author: TanB
* Created: 7/12/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

from datetime import datetime
import requests
#we will make a list of various coins to track
coins = ['BTC-USD', 'ETH-USD', 'SOL-USD','TOSHI-USD', 'DOGE-USD', 'CRO-USD', 'VET-USD',  'PENGU-USD',  'TURBO-USD']
previous_prices = {} 


with open('tstCoins.csv', 'a') as file:
    file.write('timestamp,coin,price\n')# also \n to add btc on a new line

#we will loop throu up to y coins for now
for coin in coins[:10]:
    url = f'https://api.coinbase.com/v2/prices/{coin}/spot'# 
    response = requests.get(url)
              
    
    if response.status_code == 200:
        data = response.json()
        price = data['data']['amount']
        timestamp = datetime.now().strftime('%a-%m-%d-%Y %H:%M:%S')
       
        current_price = float(price)
        if coin in previous_prices:
            old_price = previous_prices[coin]
           
            if current_price > old_price:
                direction = '+'#price went up
            elif current_price < old_price:
                direction = '-'#prices went down
            else:
                direction = '->' #if price hasen't changed
            
            
            print(f'[{timestamp}]: {coin}: {price} {direction}')
        else:
            print(f'[{timestamp}]: {coin}: {price} [new]')  #new log
             
        previous_prices[coin] = current_price#saves the current price for comparison

       #logging results to csv file
        with open('tstCoins.csv', 'a') as file:
            file.write(f'{timestamp},{coin},{price}\n') # NEW LINE LOL \n    
        print(f'[{timestamp}]: {coin}:{price}') 

    else:
        print(f'error with {coin}')   

with open('tstCoins.csv', 'a') as file:
    file.write('\n')

# https://docs.python.org/3/library/datetime.html#format-codes
# https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-all-known-trading-pairs
# https://docs.python.org/3/library/functions.html#open 
#https://docs.python.org/3/library/string.html#format-specification-mini-language
# https://docs.python.org/3/library/stdtypes.html#str
 #--------------------------------------------------

 #added time stamps and Logging 7/13/2025.
 
 #added a change in price checker, but it's not like I thought 7/16/2025
 
 # more to do