import yfinance as yf
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

data = yf.download("AAPL", start="2020-01-01", end="2025-01-01")

data["SMA20"] = data["Close"].rolling(window=20).mean()
data["SMA50"] = data["Close"].rolling(window=50).mean()

data["Signal"] = 0 
data.loc[data["SMA20"] > data["SMA50"], "Signal"] = 1 
data.loc[data["SMA20"] <= data["SMA50"], "Signal"] = -1

data["Returns"] = data["Close"].pct_change()

data["Strategy_Returns"] = data["Signal"].shift(1) * data["Returns"]

strategy_performance = (1 + data["Strategy_Returns"]).cumprod()
buy_hold = (1 + data["Returns"]).cumprod()

plt.figure(figsize=(12,6))

plt.plot(strategy_performance, label="Strategy") 
plt.plot(buy_hold, label = "Buy and Hold") 

plt.title("Trading Strategy Performance") 
plt.xlabel("Date")
plt.ylabel("Growth") 

plt.legend()

plt.show()
