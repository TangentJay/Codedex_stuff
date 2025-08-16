# statistics/tstfin.py
'''
* Author: TanB
* Created: 8/14/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

import yfinance as yf
import pandas as pd

# 1. Download historical stock data
symbol = 'TSLA'  # Tesla stock
data = yf.download(symbol, period='1mo', interval='1d')  # 1 month, daily data

# 2. Calculate a simple moving average (SMA)
window = 5  # 5-day SMA
data['SMA'] = data['Close'].rolling(window=window).mean()

# 3. Generate basic signals
# Buy if Close > SMA, Sell if Close < SMA
data['Signal'] = 0
# Only calculate signals for rows where SMA is not NaN
data.loc[data['SMA'].notna() & (data['Close'] > data['SMA']), 'Signal'] = 1   # Buy
data.loc[data['SMA'].notna() & (data['Close'] < data['SMA']), 'Signal'] = -1  # Sell

# 4. Print the last 10 rows to see signals
print(data[['Close', 'SMA', 'Signal']].tail(10))
