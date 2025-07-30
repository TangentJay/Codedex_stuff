# projects/flask/btc_app.py
'''
* Author: TanB
* Created: 7/25/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    coins = ['BTC-USD', 'ETH-USD', 'SOL-USD']
    prices = []

    for coin in coins:
        url = f'https://api.coinbase.com/v2/prices/{coin}/spot'
        try:
            response = requests.get(url)
            data = response.json()
            price = data['data']['amount']
            timestamp = datetime.now().strftime('%a-%m-%d-%Y %H:%M:%S')
            prices.append({'coin': coin, 'price': price, 'timestamp': timestamp})
        except Exception as e:
            prices.append({'coin': coin, 'price': 'Error', 'timestamp': 'N/A'})

    return render_template('index.html', prices=prices)

if __name__ == '__main__':
    app.run(debug=True)
