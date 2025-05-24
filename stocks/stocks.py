import yfinance as yf

def get_stock_data_dict(symbols):
    results = []
    for symbol in symbols:
        try:
            # Fetch all available historical data
            stock_data = yf.download(symbol, period="max")

            if stock_data.empty:
                print(f"Error: No data found for symbol {symbol}")
                continue  # Skip to the next symbol

            # Calculate the all-time high
            all_time_high = stock_data['High'].max()

            # Get the current price (last available closing price)
            current_price = stock_data['Close'].iloc[-1]

            results.append({
                'symbol': symbol,
                'high': all_time_high,
                'current': current_price
            })

        except Exception as e:
            print(f"Error processing {symbol}: {e}")
            continue  # Skip to the next symbol

    return results

# Example usage:
if __name__ == "__main__":
    stock_list = tickers = [
    'A', 'AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AEP', 
    'AIG', 'AMAT', 'AMD', 'AMGN', 'AMT', 'AMZN', 'APD', 'AVGO', 'AXP', 'BA',
    'BAC', 'BDX','BIIB', 'BK', 'BKNG', 'BLK', 'BMY', 'BRK.B', 'BSX', 'BWA','C', 'CAT',
    'CB', 'CDNS','CHTR', 'CI', 'CL', 'CMCSA', 'CMG','COF', 'COP', 'COST', 'CPRT', 'CRM',
    'CSCO', 'CVS', 'CVX', 'D', 'DAL', 'DD', 'DE', 'DHR', 'DIS', 'DOW',
    'DUK', 'DVA', 'DVN', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL',
    'EMR', 'EOG', 'EQIX', 'EQR', 'ES', 'ESS', 'ETN', 'ETR', 'EW', 'EXC',
    'EXPE', 'EXPD', 'F', 'FBHS', 'FCX', 'FDX', 'FE', 'FIS', 'FISV', 'FITB',
    'FLT', 'FMC', 'FOX', 'FOXA', 'FRC', 'FTNT', 'GD', 'GE', 'GILD', 'GIS',
    'GLW', 'GM', 'GOOG', 'GOOGL', 'GPC', 'GPN', 'GS', 'GWW', 'HAL', 'HAS',
    'HBAN', 'HCA', 'HD', 'HES', 'HIG', 'HOLX', 'HON', 'HPQ', 'HRL', 'HSY',
    'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INTC', 'INTU', 'IP',
    'IPG', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'J', 'JBHT',
    'JCI', 'JKHY', 'JNJ', 'JPM', 'K', 'KEY', 'KEYS', 'KHC', 'KMI', 'KMX',
    'KO', 'KR', 'L', 'LH', 'LHX', 'LIN', 'LLY', 'LMT', 'LNC', 'LOW',
    'LRCX', 'LUMN', 'LUV', 'LVS', 'LW', 'LYB', 'M', 'MA', 'MCD', 'MCHP',
    'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MKTX', 'MLM',
    'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MPC', 'MRK', 'MRNA', 'MRO', 'MS',
    'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'NCLH', 'NDAQ', 'NEE', 'NEM',
    'NFLX', 'NI', 'NKE', 'NOC', 'NOW', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE',
    'NVDA', 'NVR', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORCL', 'ORLY',
    'OTIS', 'OXY', 'PAYX', 'PCAR', 'PEAK', 'PEG', 'PEP', 'PFE', 'PFG', 'PG',
    'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW',
    'PPG', 'PPL', 'PRU', 'PSA', 'PSX', 'PTC', 'PVH', 'PWR', 'PYPL', 'QCOM',
    'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHHBY','RHI', 'RJF', 'RL', 'RMD',
    'ROK', 'ROL', 'ROP', 'ROST', 'RSG', 'RTX', 'SBAC', 'SBUX', 'SCHW', 'SEE',
    'SHW', 'SIVB', 'SJM', 'SLB', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE',
    'STE', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T',
    'TAP', 'TDG', 'TDY', 'TEL', 'TER', 'TFC', 'TFX', 'TGT', 'TJX', 'TMO',
    'TMUS', 'TPR', 'TRMB', 'TROW', 'TRV', 'TSCO', 'TSLA', 'TSN', 'TT', 'TTWO',
    'TWTR', 'TXN', 'TXT', 'TYL', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNP',
    'UPS', 'URI', 'USB', 'V', 'VFC', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN',
    'VRTX', 'VTR', 'VTRS', 'VZ', 'WAB', 'WAT', 'WBA', 'WDC', 'WEC', 'WELL',
    'WFC', 'WHR', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WST', 'WU', 'WY',
    'WYNN', 'XEL', 'XLNX', 'XOM', 'XRAY', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION',
    'ZTS'
]
    
    
    
    
    

 # Example list of stocks

    stock_data = get_stock_data_dict(stock_list)

    if stock_data:
        print(stock_data)
    else:
        print("Could not retrieve stock data for any of the symbols.")




