import yfinance as yf
import pandas as pd

supported_tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS"]

def get_stock_data(ticker : str, start_date : str, end_date : str) -> dict:
    """
    Fetch historical stock data for a given ticker symbol between specified dates.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple).
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: A DataFrame containing the historical stock data.
    """
    ticker = ticker.upper()  # Ensure ticker is in uppercase
    if ticker not in supported_tickers:
        raise ValueError(f"Ticker '{ticker}' is not supported.")
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    if data.empty:
        raise ValueError(f"No data found for ticker '{ticker}' between {start_date} and {end_date}.")
    data = data.reset_index()  # Reset index to have 'Date' as a column
    return {
        "symbol": ticker,
        "start_date": start_date,
        "end_date": end_date,
        "period": f"{start_date} to {end_date}",    
        "currency": stock.info.get("currency", "N/A"),  # Get currency from stock info
        "data": pd.DataFrame([
            {
                "date": row["Date"].strftime("%Y-%m-%d"),
                "open": round(float(row["Open"]), 2),
                "high": round(float(row["High"]), 2),
                "low": round(float(row["Low"]), 2),
                "close": round(float(row["Close"]), 2),
                "volume": int(row["Volume"])
            }
            for index, row in data.iterrows()
        ])
    }

if __name__ == "__main__":
    result = get_stock_data("RELIANCE.NS", "2023-01-01", "2023-12-31")
    print("Company:", result["symbol"])
    print("Data Type:", type(result["data"]))
    print("Records:", len(result["data"]))
    print("Latest:", result["data"].iloc[-1])

def calculate_volatility(prices: pd.Series) -> float:
    """
    Calculate the annualized volatility of a stock based on its price series.

    Args:
        prices (pd.Series): A pandas Series containing the stock prices.

    Returns:
        float: The annualized volatility as a decimal (e.g., 0.20 for 20%).
    """
    # 1. Validate prices
    if prices is None or len(prices) < 2:
        raise ValueError("At least two valid prices are required.")

    if prices.isna().any():
        raise ValueError("Prices must not contain missing values.")

    if (prices <= 0).any():
        raise ValueError("All prices must be greater than zero.")

    # Sort indices to ensure start and end positions match chronological timeline
    prices = prices.sort_index()

    # 2. Calculate daily returns
    daily_returns = prices.pct_change().dropna()

    # 3. Calculate annualized volatility
    annualized_volatility = daily_returns.std() * (252 ** 0.5)  # Assuming 252 trading days in a year

    return float(annualized_volatility)