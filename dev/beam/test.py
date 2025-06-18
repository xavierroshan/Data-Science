import requests
import json

url = "https://finnhub.io/api/v1/global-filings/search?token=d17d8g9r01qtc1t7l3sgd17d8g9r01qtc1t7l3t0"

payload = json.dumps({
  "query": "artificial intelligence",
  "symbols": "AAPL,GOOGL,TSLA",
  "fromDate": "2024-01-01",
  "toDate": "2025-05-30"
})


response = requests.request("POST", url, data=payload)

print(response.json())
