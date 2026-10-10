import pandas as pd

def calculate_total_returns(prices: pd.Series, dividends: pd.Series | None) -> float:
    """
    Calculate the total returns of a stock based on its price series.

    Args:
        prices (pd.Series): A pandas Series containing the stock prices.
        dividends (pd.Series | None): A pandas Series containing the dividend payments or None.

    Returns:
        float: The total returns as a decimal (e.g., 0.25 for 25%).
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

    initial_price = prices.iloc[0]
    final_price = prices.iloc[-1]

    # 2. Handle missing or empty dividend series
    if dividends is None or dividends.empty:
        return float((final_price - initial_price) / initial_price)

    if dividends.isna().any():
        raise ValueError("Dividends must not contain missing values.")

    # 3. Slice dividends safely within the active timeline
    dividends = dividends.sort_index()
    start_date = prices.index[0]
    end_date = prices.index[-1]
    
    # Using slice intersection to cleanly avoid indexing KeyErrors
    period_dividends = dividends.loc[start_date:end_date]
    
    # 4. Final Calculation
    total_returns = ((final_price - initial_price) + period_dividends.sum()) / initial_price
    return float(total_returns)


def calculate_price_cagr(prices: pd.Series) -> float:
    """
    Calculate the Compound Annual Growth Rate (CAGR) of a stock based on its price series.

    Args:
        prices (pd.Series): A pandas Series containing the stock prices.

    Returns:
        float: The CAGR as a decimal (e.g., 0.10 for 10%).
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

    initial_price = prices.iloc[0]
    final_price = prices.iloc[-1]

    # 2. Calculate the number of years between the first and last price
    start_date = prices.index[0]
    end_date = prices.index[-1]
    
    # Ensure that the index is a datetime type for accurate year calculation
    if not pd.api.types.is_datetime64_any_dtype(prices.index):
        raise TypeError("Price index must be of datetime type.")

    years = (end_date - start_date).days / 365.25  # Using average year length to account for leap years

    if years <= 0:
        raise ValueError("The time span between the first and last price must be greater than zero.")

    # 3. Final Calculation
    cagr = (final_price / initial_price) ** (1 / years) - 1
    return float(cagr)


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