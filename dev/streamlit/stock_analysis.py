import yfinance as yf
data = yf.download("AAPL", start="2022-01-01", end="2022-12-31")
print(data.head())
