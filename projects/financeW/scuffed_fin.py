from flask import Flask, render_template, request, send_file
import yfinance as yf
import mplfinance as mpf
import pandas as pd
from datetime import datetime, timedelta
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart', methods=['POST'])
def generate_chart():
    # Get user input
    ticker = request.form['ticker'].upper()
    period = request.form.get('period', '11mo')
    
    try:
        # Fetch data
        data = yf.download(ticker, period=period)
        4
        # Clean data
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.droplevel(1)
        
        data_clean = data[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()
        
        # Create chart in memory (no file saved)
        buf = io.BytesIO()
        mpf.plot(data_clean,
                 type='candle',
                 volume=True,
                 style='nightclouds',
                 title=f'{ticker}  Price',
                 ylabel='Price ($)',
                 savefig=dict(fname=buf, dpi=100, bbox_inches='tight'),
                 show_nontrading=False)
        
        buf.seek(0)
        return send_file(buf, mimetype='image/png', download_name=f'{ticker}_chart.png')
        
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)