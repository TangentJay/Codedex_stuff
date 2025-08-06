# cryptobot/crypto_track1.py
'''
* Author: TanB
* Created: 8/5/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import time
from datetime import datetime
import requests
#we will make a list of various coins to track
coins = ['BTC-USD', 'ETH-USD', 'SOL-USD','TOSHI-USD', 'DOGE-USD', 'CRO-USD', 'VET-USD',  'PENGU-USD',  'TURBO-USD','XRP-USD']
previous_prices = {} 


with open('tstCoins.csv', 'a') as file:
    file.write('timestamp,coin,price\n')# also \n to add btc on a new line

#we will loop throu up to y coins for now
try:
    while True:
        print(f'\n*** Updated at {datetime.now().strftime('%H:%M:%S')} ***\n')
        with open('tstCoins.csv', 'a')as file:

            for coin in coins[:20]:
                url = f'https://api.coinbase.com/v2/prices/{coin}/spot'# 
                response = requests.get(url)
                        
                
                if response.status_code == 200:
                    data = response.json()
                    price = data['data']['amount']
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
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
                    
                    file.write(f'{timestamp},{coin},{price}\n') # NEW LINE LOL \n    
                    print(f'[{timestamp}]: {coin}:{price}') 

                else:
                    print(f'error with {coin}')   

        
        print('waiting 9 sec')
        time.sleep(9)

except KeyboardInterrupt:
    print('stopped')        
# https://docs.python.org/3/library/datetime.html#format-codes
# https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-all-known-trading-pairs
# https://docs.python.org/3/library/functions.html#open 
# https://docs.python.org/3/library/string.html#format-specification-mini-language
# https://docs.python.org/3/library/stdtypes.html#str
# https://docs.python.org/3/library/time.html
 #--------------------------------------------------

 #added time stamps and Logging 7/13/2025.
 
 #added a change in price checker, but it's not like I thought 7/16/2025
 
 #8/5/2025 improved while loop and added time.sleep. will adjust as I see fit. Added try/except 
 # more to do
