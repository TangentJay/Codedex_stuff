# 192.168.0.0 to 192.168.255.255 - Home/small networks
# 10.0.0.0 to 10.255.255.255 - Large private networks
# 172.16.0.0 to 172.31.255.255 - Medium networks

# ============================================================================
# LEARNING NOTES FOR FUTURE PROJECTS
# ============================================================================
"""
KEY CONCEPTS YOU LEARNED:

1. STREAMLIT BASICS:
   - st.title(), st.header() - Text headers
   - st.number_input(), st.text_input() - User inputs
   - st.button() - Clickable buttons
   - st.columns() - Layout in columns
   - st.metric() - Display metrics with deltas
   - st.plotly_chart() - Display charts

2. PANDAS (DATA MANIPULATION):
   - DataFrame - Like an Excel spreadsheet
   - .iloc[index] - Get row by position
   - .reset_index() - Make index a regular column

3. YFINANCE (STOCK DATA):
   - yf.Ticker(symbol) - Create stock object
   - .history() - Get historical prices

4. PLOTLY (CHARTS):
   - go.Figure() - Create chart
   - go.Scatter() - Line chart
   - add_hline() - Horizontal line

5. PYTHON BASICS:
   - Functions with def
   - Dictionaries with {}
   - String formatting with f"{variable:.2f}"
   - try/except for error handling

NEXT STEPS:
- Add more chart types (candlestick charts)
- Save/load trade simulations
- Add technical indicators (RSI, MACD)
- Compare multiple stocks
- Export results to CSV
"""