import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker, period='1y'):
    """
    Fetch historical stock data for a given ticker.
    :param ticker: Stock symbol (e.g., 'AAPL' for Apple)
    :param period: Time period (e.g., '1y' for 1 year)
    :return: DataFrame with historical data
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

def display_stock_info(ticker):
    """
    Display key information about the stock.
    :param ticker: Stock symbol
    """
    stock = yf.Ticker(ticker)
    info = stock.info
    print("\n=== Stock Information ===")
    print(f"Name: {info.get('longName', 'N/A')}")
    print(f"Sector: {info.get('sector', 'N/A')}")
    print(f"Current Price: {info.get('currentPrice', 'N/A')} USD")
    print(f"Market Cap: {info.get('marketCap', 'N/A')} USD")
    print(f"52-Week High: {info.get('fiftyTwoWeekHigh', 'N/A')} USD")
    print(f"52-Week Low: {info.get('fiftyTwoWeekLow', 'N/A')} USD")
    print(f"Dividend Yield: {info.get('dividendYield', 'N/A')}")

def plot_stock_trend(data, ticker):
    """
    Plot the stock's closing price trend.
    :param data: DataFrame with historical data
    :param ticker: Stock symbol
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Closing Price', color='blue')
    plt.title(f"{ticker} Stock Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("=== Stock Market Analyzer ===")
    ticker = input("Enter the stock ticker (e.g., SOFI, MSFT, GOOGL, AAPL, NVDA): ").upper()

    # Fetch and display stock data
    data = fetch_stock_data(ticker)
    display_stock_info(ticker)

    # Plot the stock trend
    plot_stock_trend(data, ticker)

    # Additional analysis
    print("\n=== Additional Analysis ===")
    print(f"Average Closing Price (Last Year): {data['Close'].mean():.2f} USD")
    print(f"Highest Closing Price (Last Year): {data['Close'].max():.2f} USD")
    print(f"Lowest Closing Price (Last Year): {data['Close'].min():.2f} USD")

if __name__ == "__main__":
    main()