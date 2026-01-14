# # Auto-trader: Flowchart + Example Python Script

# ## Purpose

# This document shows a clear flowchart for a simple rule-based auto-trading script (buy between $0.40–$0.44, sell at $0.50) and a beginner-friendly example Python script with detailed comments. The code is written for learning and simulation — **do not** run it against a live broker until you fully understand each part and use a paper-trading API.

# ---

# ## Flowchart (ASCII)

# ```
# [Start]
#    |
#    v
# [Load config: symbol, buy_range, sell_price, trade_amount, max_trades_per_day, mode]
#    |
#    v
# [Connect to data source / API (or simulation)]
#    |
#    v
# [Loop while market open and not exceeded max trades]
#    |
#    v
# [Get current price]
#    |
#    +--> Is price <= buy_threshold?
#    |       | Yes
#    |       v
#    |   [Place limit buy order for available funds]
#    |       |
#    |       v
#    |   [If buy filled -> start monitoring position]
#    |       |
#    |       v
#    |   [Monitor price -> Is price >= sell_price?]
#    |       | Yes
#    |       v
#    |   [Place limit/market sell order]
#    |       |
#    |       v
#    |   [Record trade, update capital, increment trades_today]
#    |       |
#    |       v
#    +-------+-----------------------------------------------+
#            | No                                            |
#            v                                               v
#    [Wait small interval]                           [Check risk / stop-loss]
#            |                                               |
#            v                                               v
#    [Loop back to Get current price]                 [If stop-loss hit -> sell -> record]
#                                                         |
#                                                         v
#                                               [Loop back to Get current price]

# ```

# ---

# ## Key Logic Steps (plain language)

# 1. Load parameters: symbol, min_buy_price, max_buy_price, target_sell_price, capital_to_use (e.g. $2000), max_trades/day, stop_loss_pct, paper_trade flag.
# 2. Compute how many shares to buy: `shares = floor(capital / buy_price)`.
# 3. Attempt to place a limit buy at or below the configured buy price.
# 4. If filled, immediately monitor the position for reaching the sell target or stop-loss.
# 5. When sell condition met, place order and record the trade P&L.
# 6. Enforce safety limits: max trades/day, min capital, not using margin unless you understand PDT rules.
# 7. Loop until market close or stop condition.

# ---

# ## Important Safety & Practical Notes

# * **Pattern Day Trading (PDT):** If you have under $25,000 in a margin account and make 4+ day trades in 5 business days, you may be restricted. Add logic to count same-day round-trip trades if you plan to day trade.
# * **Robinhood caution:** Robinhood does not provide an official public trading API for automated retail trading. Using unofficial APIs may violate terms of service. Use a paper-trading API such as Alpaca or your broker's official sandbox for development.
# * **Slippage & fills:** Limit orders might not fill. Consider adding timeouts and fallback logic (e.g., cancel limit and place a market order if needed — but this increases risk).
# * **Taxes & fees:** Gains are taxable; frequent trading has tax implications.
# * **Simulation first:** Run the script in `paper_trade` mode that never touches a live account.
# * **Charting:** For analysis, use line charts, candlestick charts, volume bars, moving averages, and indicators like RSI/MACD. Pie charts are not typically useful for price movement.

# ---

# ## Example Python Script (educational, simulated/paper-trading)

# # ```python
# # auto_trader_example.py
# # Beginner-friendly example of a rule-based auto-trader simulation.
# # Uses single quotes for string literals per user preference.
# # THIS IS FOR LEARNING / SIMULATION. Replace the placeholder API functions
# # with real broker API calls only after testing with paper trading.

import time
import math
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

# ------------------------
# Configuration (change these)
# ------------------------
CONFIG = {
    'symbol': 'GPUS',                   # stock ticker
    'min_buy_price': 0.40,             # lower bound where we'll buy
    'max_buy_price': 0.44,             # upper bound where we'll buy
    'target_sell_price': 0.50,         # price where we'll take profit
    'capital_per_trade': 2000.00,      # USD allocated per trade
    'max_trades_per_day': 3,           # safety limit to avoid PDT-like behavior
    'stop_loss_pct': 0.10,             # 10% stop-loss from buy price
    'poll_interval_sec': 5,            # how often to check price
    'paper_trade': True,               # True -> simulate trades locally
}

# ------------------------
# Simple in-memory state
# ------------------------
state = {
    'trades_today': 0,
    'cash': CONFIG['capital_per_trade'],
    'positions': {},  # keyed by symbol
    'trade_log': [],
    'price_history': []  # store prices for charting
}

# ------------------------
# Placeholder functions for simulation
# ------------------------

def fetch_current_price(symbol):
    # Placeholder: simulate a price; in real code, fetch from API
    import random
    price = round(random.uniform(0.40, 0.51), 2)
    state['price_history'].append(price)
    return price


def place_limit_buy(symbol, price, shares, paper_trade=True):
    market_price = fetch_current_price(symbol)
    if paper_trade and market_price <= price:
        return {'status': 'filled', 'executed_price': market_price}
    return {'status': 'open', 'executed_price': None}


def place_market_sell(symbol, shares, paper_trade=True):
    market_price = fetch_current_price(symbol)
    if paper_trade:
        return {'status': 'filled', 'executed_price': market_price}
    return {'status': 'open', 'executed_price': None}

# ------------------------
# Trading logic functions
# ------------------------

def compute_shares_for_capital(capital, buy_price):
    return math.floor(capital / buy_price)


def try_buy_once(symbol):
    if state['trades_today'] >= CONFIG['max_trades_per_day']:
        return None

    price = fetch_current_price(symbol)
    if CONFIG['min_buy_price'] <= price <= CONFIG['max_buy_price']:
        shares = compute_shares_for_capital(CONFIG['capital_per_trade'], price)
        if shares <= 0:
            return None

        result = place_limit_buy(symbol, price, shares, paper_trade=CONFIG['paper_trade'])
        if result['status'] == 'filled':
            state['positions'][symbol] = {
                'shares': shares,
                'buy_price': result['executed_price'],
                'buy_time': datetime.utcnow(),
            }
            state['trades_today'] += 1
            return {'action': 'buy', 'shares': shares, 'price': result['executed_price']}
    return None


def monitor_and_sell_if_target_hit(symbol):
    pos = state['positions'].get(symbol)
    if not pos:
        return None

    current_price = fetch_current_price(symbol)
    buy_price = pos['buy_price']
    shares = pos['shares']

    if current_price >= CONFIG['target_sell_price'] or current_price <= buy_price * (1 - CONFIG['stop_loss_pct']):
        sell_result = place_market_sell(symbol, shares, paper_trade=CONFIG['paper_trade'])
        if sell_result['status'] == 'filled':
            executed_price = sell_result['executed_price']
            pnl = (executed_price - buy_price) * shares
            record = {
                'symbol': symbol,
                'shares': shares,
                'buy_price': buy_price,
                'sell_price': executed_price,
                'pnl': pnl,
                'buy_time': pos['buy_time'],
                'sell_time': datetime.utcnow(),
            }
            state['trade_log'].append(record)
            state['positions'].pop(symbol, None)
            return record
    return None

# ------------------------
# Main loop
# ------------------------

def main_loop():
    symbol = CONFIG['symbol']
    for _ in range(200):  # simulation loop
        if symbol not in state['positions']:
            try_buy_once(symbol)
        monitor_and_sell_if_target_hit(symbol)
        time.sleep(CONFIG['poll_interval_sec'])

    print('Trade log:', state['trade_log'])
    plot_price_history(symbol)

# ------------------------
# Charting function
# ------------------------

def plot_price_history(symbol):
    df = pd.DataFrame(state['price_history'], columns=['Price'])
    df['Index'] = df.index

    plt.figure(figsize=(10, 5))
    plt.plot(df['Index'], df['Price'], label='Price')
    plt.title(f'{symbol} Price History (Simulation)')
    plt.xlabel('Time steps')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show()

# ------------------------
# Run simulation
# ------------------------

if __name__ == '__main__':
    main_loop()


