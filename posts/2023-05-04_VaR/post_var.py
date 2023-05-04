import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# Read data
ibov = yf.download("^BVSP", start="2010-01-01", end="2021-05-01")
ibov_close_prices = ibov["Adj Close"]

ibov_close_prices.plot()
plt.show()

# Calculate returns
ibov_returns = ibov_close_prices.pct_change().dropna()
ibov_returns.hist(bins=100)

print(ibov_returns.describe())
print(ibov_returns.mean())
print(ibov_returns.std())

plt.show()

print("stop here")
