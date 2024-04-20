import alpaca_trade_api as tradeapi
import time

# Alpaca API credential
API_KEY = ''
SECRET_KEY = ''
BASE_URL = 'https://paper-api.alpaca.markets'  # For paper trading, replace with live URL for real trading

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')  # Initialize Alpaca API

def buy(symbol, qty):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print(f"Bought {qty} shares of {symbol}")
    except Exception as e:
        print(f"Failed to buy {qty} shares of {symbol}: {str(e)}")

def sell(symbol, qty):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        print(f"Sold {qty} shares of {symbol}")
    except Exception as e:
        print(f"Failed to sell {qty} shares of {symbol}: {str(e)}")

def check_prices(symbol):
    try:
        bars = api.get_barset(symbol, 'minute', limit=5)
        latest_bar = bars[symbol][-1]
        latest_close = latest_bar.c
        return latest_close
    except Exception as e:
        print(f"Failed to get price data for {symbol}: {str(e)}")

def main():
    symbol = 'AAPL' #Replace with any ticker 
    while True:
        current_price = check_prices(symbol)
        if current_price is not None:
            if current_price < 100: 
                buy(symbol, 1) 
            elif current_price > 150:
                sell(symbol, 1) 
        time.sleep(60)  

if __name__ == "__main__":
    main()
