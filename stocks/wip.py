import requests
import pandas as pd
from datetime import datetime, timedelta

# Replace this with your actual Tiingo API Key
API_KEY = "8f19a382b1de3d52beb5d4d4e62eae0b38702a2a"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_KEY}"
}

companies = [
    {"Company_name": "Apple", "ticker": "AAPL"}
]

def get_current_price(ticker):
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()[0].get("close", None)
    else:
        print(f"Error fetching current price for {ticker}: {response.status_code} - {response.text}")
    return None

def get_high_since(ticker, start_date):
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate={start_date}"
    response = requests.get(url, headers=headers)
    if response.ok:
        prices = [d['high'] for d in response.json() if 'high' in d]
        return max(prices) if prices else None
    else:
        print(f"Error fetching highs for {ticker}: {response.status_code} - {response.text}")
    return None

def get_fundamentals(ticker):
    url = f"https://api.tiingo.com/tiingo/fundamentals/{ticker}/statements?statements=income_statement&limit=1"
    response = requests.get(url, headers=headers)
    if response.ok:
        json_data = response.json()
        if json_data and 'data' in json_data[0] and json_data[0]['data']:
            data = json_data[0]['data'][0]
            return {
                "Net Profit": data.get("netIncome", None),
                "EBIT": data.get("operatingIncome", None)
            }
        else:
            print(f"No income statement data for {ticker}")
    else:
        print(f"Error fetching fundamentals for {ticker}: {response.status_code} - {response.text}")
    return {"Net Profit": None, "EBIT": None}

def get_pe_marketcap(ticker):
    url = f"https://api.tiingo.com/tiingo/fundamentals/{ticker}/daily"
    response = requests.get(url, headers=headers)
    if response.ok:
        data = response.json()
        return {
            "Market Cap": data.get("marketCap", None),
            "PE Ratio": data.get("peRatio", None)
        }
    else:
        print(f"Error fetching market cap/PE for {ticker}: {response.status_code} - {response.text}")
    return {"Market Cap": None, "PE Ratio": None}

# Dates for highs
one_year_ago = (datetime.now() - timedelta(days=365)).date().isoformat()
two_years_ago = (datetime.now() - timedelta(days=2 * 365)).date().isoformat()
five_years_ago = (datetime.now() - timedelta(days=5 * 365)).date().isoformat()

# Results list
results = []

# Loop over companies
for company in companies:
    ticker = company["ticker"]
    print(f"Fetching data for {ticker}...")

    current_price = get_current_price(ticker)
    high_1y = get_high_since(ticker, one_year_ago)
    high_2y = get_high_since(ticker, two_years_ago)
    high_5y = get_high_since(ticker, five_years_ago)
    fundamentals = get_fundamentals(ticker)
    pe_and_mc = get_pe_marketcap(ticker)

    results.append({
        "Company": company["Company_name"],
        "Ticker": ticker,
        "Current Price": current_price,
        "Market Cap": pe_and_mc["Market Cap"],
        "PE Ratio": pe_and_mc["PE Ratio"],
        "Net Profit": fundamentals["Net Profit"],
        "EBIT": fundamentals["EBIT"],
        "1Y High": high_1y,
        "2Y High": high_2y,
        "5Y High": high_5y
    })

# Convert to DataFrame
df = pd.DataFrame(results)

# Print or save
print(df)
# df.to_csv("stock_summary.csv", index=False)  # Uncomment to save
