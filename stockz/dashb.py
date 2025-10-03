"""
STOCK TRADING ANALYSIS DASHBOARD
==================================
A Python dashboard for analyzing stock trades and historical price movements.

REQUIRED LIBRARIES:
Install these before running:
    pip install streamlit yfinance pandas plotly

HOW TO RUN:
    streamlit run stock_dashboard.py

WHAT THIS DOES:
1. Trade Calculator: Calculate gains/losses from buy/sell prices
2. Historical Analysis: Fetch real stock data and analyze price movements
"""

# ============================================================================
# SECTION 1: IMPORT LIBRARIES
# ============================================================================

import streamlit as st  # Web app framework - creates the interface
import yfinance as yf   # Downloads stock data from Yahoo Finance (free!)
import pandas as pd     # Data manipulation - think of it like Excel in Python
import plotly.graph_objects as go  # Interactive charts
from datetime import datetime, timedelta  # Work with dates
import numpy as np      # Numerical operations

# ============================================================================
# SECTION 2: PAGE CONFIGURATION
# ============================================================================

# Set up the page - this MUST be the first Streamlit command
st.set_page_config(
    page_title="Stock Trading Dashboard",  # Browser tab title
    page_icon="📈",  # Browser tab icon
    layout="wide"    # Use full width of browser
)

# ============================================================================
# SECTION 3: HELPER FUNCTIONS
# ============================================================================

def calculate_trade_metrics(entry_price, exit_price, capital):
    """
    Calculate trading metrics from entry/exit prices and capital.
    
    PARAMETERS:
        entry_price (float): Price you bought at
        exit_price (float): Price you sold at
        capital (float): Money you invested
    
    RETURNS:
        dict: Dictionary with all calculated metrics
        
    HOW IT WORKS:
        1. Calculate how many shares you can buy: capital / entry_price
        2. Calculate absolute gain: (exit - entry) × shares
        3. Calculate percentage gain: ((exit - entry) / entry) × 100
    """
    
    # Calculate number of shares (capital divided by entry price)
    shares = capital / entry_price
    
    # Calculate dollar gain/loss
    # Formula: (price difference) × (number of shares)
    absolute_gain = (exit_price - entry_price) * shares
    
    # Calculate percentage gain/loss
    # Formula: ((new price - old price) / old price) × 100
    percent_gain = ((exit_price - entry_price) / entry_price) * 100
    
    # Calculate final portfolio value
    final_value = capital + absolute_gain
    
    # Return all results as a dictionary (key-value pairs)
    return {
        'shares': shares,
        'absolute_gain': absolute_gain,
        'percent_gain': percent_gain,
        'initial_capital': capital,
        'final_value': final_value
    }


def fetch_stock_data(ticker, days=90):
    """
    Fetch historical stock price data from Yahoo Finance.
    
    PARAMETERS:
        ticker (str): Stock symbol (e.g., 'AAPL', 'GPUS')
        days (int): Number of days of history to fetch
    
    RETURNS:
        pandas.DataFrame: Table with dates and prices
        
    HOW IT WORKS:
        1. Calculate the start date (today - days)
        2. Use yfinance to download data
        3. Return as a pandas DataFrame (like an Excel table)
    """
    
    try:
        # Calculate date range
        # datetime.now() gets current date/time
        # timedelta(days=days) creates a time difference
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Download stock data using yfinance
        # Ticker creates a stock object
        # .history() downloads historical prices
        stock = yf.Ticker(ticker)
        df = stock.history(start=start_date, end=end_date)
        
        # Check if we got any data
        if df.empty:
            return None
        
        # Reset index so 'Date' becomes a regular column (not the index)
        df.reset_index(inplace=True)
        
        return df
        
    except Exception as e:
        # If anything goes wrong, print error and return None
        st.error(f"Error fetching data: {str(e)}")
        return None


def calculate_price_movement(df, start_days_ago, end_days_ago):
    """
    Calculate price change between two points in time.
    
    PARAMETERS:
        df (DataFrame): Stock price data
        start_days_ago (int): How many days back for start point
        end_days_ago (int): How many days back for end point
    
    RETURNS:
        dict: Dictionary with price movement info
        
    HOW IT WORKS:
        1. Find the row at 'start_days_ago' position
        2. Find the row at 'end_days_ago' position
        3. Calculate the difference and percentage change
    """
    
    # Get total number of rows (days of data)
    total_rows = len(df)
    
    # Calculate index positions
    # If we have 90 days of data and want "30 days ago":
    # start_index = 90 - 30 - 1 = 59 (we subtract 1 because arrays start at 0)
    start_index = max(0, total_rows - start_days_ago - 1)
    end_index = max(0, total_rows - end_days_ago - 1)
    
    # Make sure indices are valid
    if start_index >= total_rows or end_index >= total_rows:
        return None
    
    # Get the closing prices at those dates
    # .iloc[index] gets the row at that position
    # ['Close'] gets the closing price column
    start_price = df.iloc[start_index]['Close']
    end_price = df.iloc[end_index]['Close']
    
    # Get the dates (convert to string for display)
    start_date = df.iloc[start_index]['Date'].strftime('%Y-%m-%d')
    end_date = df.iloc[end_index]['Date'].strftime('%Y-%m-%d')
    
    # Calculate price change (absolute and percentage)
    price_change = end_price - start_price
    percent_change = (price_change / start_price) * 100
    
    # Return all info as dictionary
    return {
        'start_date': start_date,
        'end_date': end_date,
        'start_price': start_price,
        'end_price': end_price,
        'price_change': price_change,
        'percent_change': percent_change
    }


def create_price_chart(df, entry_price=None, exit_price=None):
    """
    Create an interactive line chart of stock prices.
    
    PARAMETERS:
        df (DataFrame): Stock price data
        entry_price (float, optional): Buy price to show on chart
        exit_price (float, optional): Sell price to show on chart
    
    RETURNS:
        plotly figure: Interactive chart object
        
    HOW IT WORKS:
        1. Create a Plotly figure object
        2. Add the price line
        3. Add entry/exit lines if provided
        4. Customize appearance (colors, labels, etc.)
    """
    
    # Create a new Plotly figure
    fig = go.Figure()
    
    # Add the main price line
    # go.Scatter creates a line chart
    fig.add_trace(go.Scatter(
        x=df['Date'],           # x-axis: dates
        y=df['Close'],          # y-axis: closing prices
        mode='lines',           # Draw as a line (not points)
        name='Close Price',     # Label for legend
        line=dict(color='#3B82F6', width=2),  # Blue line, 2px wide
        fill='tozeroy',         # Fill area under line
        fillcolor='rgba(59, 130, 246, 0.1)'  # Light blue fill (rgba = red,green,blue,alpha)
    ))
    
    # Add entry price line if provided
    if entry_price is not None:
        # add_hline adds a horizontal line across the chart
        fig.add_hline(
            y=entry_price,      # y position
            line_dash="dash",   # Dashed line style
            line_color="green", # Green color
            annotation_text="Entry Price",  # Label
            annotation_position="right"
        )
    
    # Add exit price line if provided
    if exit_price is not None:
        fig.add_hline(
            y=exit_price,
            line_dash="dash",
            line_color="red",
            annotation_text="Exit Price",
            annotation_position="right"
        )
    
    # Update chart layout (appearance)
    fig.update_layout(
        title="Stock Price History",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        hovermode='x unified',  # Show all values when hovering
        plot_bgcolor='white',   # White background
        height=500              # Chart height in pixels
    )
    
    # Customize grid lines
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#E5E7EB')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#E5E7EB')
    
    return fig


# ============================================================================
# SECTION 4: MAIN APPLICATION
# ============================================================================

def main():
    """
    Main function that runs the entire dashboard.
    
    This is where we build the user interface and handle all interactions.
    """
    
    # Title and description
    st.title("📈 Stock Trading Analysis Dashboard")
    st.markdown("Simulate trades and analyze historical price movements")
    
    # Add some space
    st.markdown("---")
    
    # ========================================================================
    # PART 1: TRADE CALCULATOR
    # ========================================================================
    
    st.header("💰 Trade Calculator")
    st.markdown("Calculate potential gains/losses from a trade")
    
    # Create three columns for input fields
    # This makes them appear side-by-side
    col1, col2, col3 = st.columns(3)
    
    # Column 1: Entry Price
    with col1:
        # number_input creates a numeric input field
        entry_price = st.number_input(
            "Entry Price ($)",      # Label above input
            min_value=0.01,         # Minimum allowed value
            value=150.00,           # Default value
            step=0.01,              # Increment when using arrows
            help="Price you bought the stock at"  # Tooltip on hover
        )
    
    # Column 2: Exit Price
    with col2:
        exit_price = st.number_input(
            "Exit Price ($)",
            min_value=0.01,
            value=175.00,
            step=0.01,
            help="Price you sold the stock at"
        )
    
    # Column 3: Capital
    with col3:
        capital = st.number_input(
            "Capital Invested ($)",
            min_value=0.01,
            value=1000.00,
            step=10.00,
            help="Total money invested"
        )
    
    # Calculate button
    # When clicked, it runs the code inside the 'if' statement
    if st.button("Calculate Trade", type="primary"):
        
        # Call our calculation function
        results = calculate_trade_metrics(entry_price, exit_price, capital)
        
        # Display results in metric cards
        # st.columns creates a row of columns
        col1, col2, col3 = st.columns(3)
        
        # Each metric shows: label, value, and change (delta)
        with col1:
            st.metric(
                "Shares Purchased",
                f"{results['shares']:.2f}",  # :.2f formats to 2 decimal places
            )
        
        with col2:
            st.metric(
                "Absolute Gain",
                f"${results['absolute_gain']:.2f}",
                delta=f"{results['percent_gain']:.2f}%"  # Shows change in green/red
            )
        
        with col3:
            st.metric(
                "Final Portfolio Value",
                f"${results['final_value']:.2f}",
                delta=f"${results['absolute_gain']:.2f}"
            )
        
        # Second row of metrics
        col4, col5, col6 = st.columns(3)
        
        with col4:
            st.metric("Initial Capital", f"${results['initial_capital']:.2f}")
        
        with col5:
            st.metric("Percent Gain", f"{results['percent_gain']:.2f}%")
        
        with col6:
            st.metric("ROI", f"{results['percent_gain']:.2f}%")
    
    # Add separator
    st.markdown("---")
    
    # ========================================================================
    # PART 2: HISTORICAL ANALYSIS
    # ========================================================================
    
    st.header("📊 Historical Price Analysis")
    st.markdown("Fetch real stock data and analyze price movements")
    
    # Create input fields
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    
    with col1:
        # text_input creates a text field
        ticker = st.text_input(
            "Stock Ticker",
            value="GPUS",
            help="Enter stock symbol (e.g., AAPL, TSLA, GPUS)"
        ).upper()  # .upper() converts to uppercase
    
    with col2:
        start_days = st.number_input(
            "Start (days ago)",
            min_value=1,
            max_value=365,
            value=30,
            help="Starting point for analysis"
        )
    
    with col3:
        end_days = st.number_input(
            "End (days ago)",
            min_value=0,
            max_value=365,
            value=0,
            help="End point for analysis (0 = today)"
        )
    
    with col4:
        st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
        analyze_button = st.button("Analyze", type="primary")
    
    # When Analyze button is clicked
    if analyze_button:
        
        # Validation: start should be greater than end
        if start_days <= end_days:
            st.error("Start days must be greater than end days!")
        else:
            # Show loading spinner while fetching data
            with st.spinner(f"Fetching data for {ticker}..."):
                
                # Fetch stock data
                df = fetch_stock_data(ticker, days=max(start_days + 10, 90))
                
                # Check if we got data
                if df is not None and not df.empty:
                    
                    # Calculate price movement
                    movement = calculate_price_movement(df, start_days, end_days)
                    
                    if movement:
                        # Display results
                        st.success(f"Successfully fetched {len(df)} days of data for {ticker}")
                        
                        # Show price movement metrics
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric(
                                "Start Price",
                                f"${movement['start_price']:.2f}",
                                delta=movement['start_date']
                            )
                        
                        with col2:
                            st.metric(
                                "End Price",
                                f"${movement['end_price']:.2f}",
                                delta=movement['end_date']
                            )
                        
                        with col3:
                            st.metric(
                                "Price Change",
                                f"${movement['price_change']:.2f}",
                                delta=f"{movement['percent_change']:.2f}%"
                            )
                        
                        # Create and display chart
                        st.subheader("Price Chart")
                        
                        # Create chart (with entry/exit lines if they exist)
                        fig = create_price_chart(
                            df,
                            entry_price=entry_price if 'entry_price' in locals() else None,
                            exit_price=exit_price if 'exit_price' in locals() else None
                        )
                        
                        # Display chart
                        # use_container_width makes chart fill available space
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Optional: Show raw data table
                        with st.expander("View Raw Data"):
                            # Display DataFrame as table
                            st.dataframe(df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']])
                    
                    else:
                        st.error("Could not calculate price movement. Check your day ranges.")
                
                else:
                    st.error(f"Could not fetch data for {ticker}. Check the ticker symbol.")
    
    # ========================================================================
    # PART 3: INSTRUCTIONS
    # ========================================================================
    
    st.markdown("---")
    st.info("""
    ### 📖 How to Use This Dashboard
    
    **Trade Calculator:**
    - Enter your buy price, sell price, and invested capital
    - Click "Calculate Trade" to see potential gains/losses
    
    **Historical Analysis:**
    - Enter a stock ticker (e.g., AAPL, TSLA, GPUS)
    - Set time range (e.g., 30 days ago to today)
    - Click "Analyze" to fetch real stock data and see price movements
    
    **Tips:**
    - The chart shows entry/exit price lines if you've calculated a trade
    - All data is fetched from Yahoo Finance (free and real-time)
    - You can expand "View Raw Data" to see the full dataset
    """)


# ============================================================================
# SECTION 5: RUN THE APP
# ============================================================================

# This checks if the script is being run directly (not imported)
# If true, it runs the main() function
if __name__ == "__main__":
    main()


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