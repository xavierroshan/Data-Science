import requests
import datetime as dt
from datetime import datetime
import time
from tabulate import tabulate

ALPHA_VANTAGE_API_KEY = 'YOUR_API_KEY'  # Get free key from https://www.alphavantage.co

def get_stock_data(company):
    ticker = company['ticker']
    name = company['Company_name']
    
    # Helper function to format large numbers
    def format_large_num(num):
        if num is None:
            return 'N/A'
        if num >= 1e12:
            return f"${num/1e12:.2f}T"
        elif num >= 1e9:
            return f"${num/1e9:.2f}B"
        elif num >= 1e6:
            return f"${num/1e6:.2f}M"
        else:
            return f"${num:,.2f}"

    # 1. Get current price and historical highs
    price_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}"
    price_response = requests.get(price_url).json()
    
    if "Time Series (Daily)" not in price_response:
        print(f"Error fetching price data for {ticker}:", price_response.get('Note', 'Unknown error'))
        return None

    daily_data = price_response["Time Series (Daily)"]
    dates = sorted(daily_data.keys(), reverse=True)
    
    current_price = float(daily_data[dates[0]]["4. close"])
    
    # Calculate historical highs
    today = datetime.now().date()
    one_year_ago = today - dt.timedelta(days=365)
    two_years_ago = today - dt.timedelta(days=365*2)
    five_years_ago = today - dt.timedelta(days=365*5)
    
    high_1y = max(float(daily_data[date]["2. high"]) for date in dates 
               if datetime.strptime(date, "%Y-%m-%d").date() >= one_year_ago)
    
    high_2y = max(float(daily_data[date]["2. high"]) for date in dates 
               if datetime.strptime(date, "%Y-%m-%d").date() >= two_years_ago)
    
    high_5y = max(float(daily_data[date]["2. high"]) for date in dates 
               if datetime.strptime(date, "%Y-%m-%d").date() >= five_years_ago)

    # 2. Get fundamental data
    overview_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}"
    overview = requests.get(overview_url).json()
    
    market_cap = float(overview.get('MarketCapitalization', 0))
    pe_ratio = overview.get('PERatio', 'N/A')
    
    # 3. Get income statement (for revenue, net income, EBIT)
    income_url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}"
    income_data = requests.get(income_url).json()
    
    if 'annualReports' in income_data and len(income_data['annualReports']) > 0:
        latest_annual = income_data['annualReports'][0]
        revenue = float(latest_annual.get('totalRevenue', 0))
        net_income = float(latest_annual.get('netIncome', 0))
        ebit = float(latest_annual.get('ebit', 0))
    else:
        revenue = net_income = ebit = None

    return {
        'Company': name,
        'Ticker': ticker,
        'Price': format_large_num(current_price),
        '1Y High': format_large_num(high_1y),
        '2Y High': format_large_num(high_2y),
        '5Y High': format_large_num(high_5y),
        'Market Cap': format_large_num(market_cap),
        'Revenue': format_large_num(revenue),
        'Net Income': format_large_num(net_income),
        'EBIT': format_large_num(ebit),
        'P/E': pe_ratio if isinstance(pe_ratio, str) else f"{pe_ratio:.2f}"
    }

# List of companies to analyze
companies = [
    {"Company_name": "Amazon", "ticker": "AMZN"},
    {"Company_name": "Mastercard", "ticker": "MA"},
    {"Company_name": "Apple", "ticker": "AAPL"},
    {"Company_name": "Microsoft", "ticker": "MSFT"},
    {"Company_name": "Alphabet", "ticker": "GOOGL"}
]

# Process all companies
results = []
for company in companies:
    print(f"Fetching data for {company['Company_name']} ({company['ticker']})...")
    data = get_stock_data(company)
    if data:
        results.append(data)
    time.sleep(12)  # Respect Alpha Vantage's 5 requests/minute limit

# Prepare table data
table_data = []
headers = ['Company', 'Ticker', 'Price', '1Y High', '2Y High', '5Y High', 
           'Market Cap', 'Revenue', 'Net Income', 'EBIT', 'P/E']

for result in results:
    table_data.append([
        result['Company'],
        result['Ticker'],
        result['Price'],
        result['1Y High'],
        result['2Y High'],
        result['5Y High'],
        result['Market Cap'],
        result['Revenue'],
        result['Net Income'],
        result['EBIT'],
        result['P/E']
    ])

# Print table
print("\nFinancial Metrics Comparison")
print("="*120)
print(tabulate(table_data, headers=headers, tablefmt='grid', stralign='right', numalign='right'))