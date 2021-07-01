import os
import requests
import json
from pprint import pprint
api_key = os.environ['ALPHA_VANTAGE']

# SMA_60_url = f'https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=daily&time_period=60&series_type=open&apikey={api_key}'
# SMA_200_url = f'https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=daily&time_period=200&series_type=open&apikey={api_key}'
# SMA_IBM_60 = requests.get(SMA_60_url)
# SMA_IBM_200 = requests.get(SMA_200_url)
# # pprint(SMA_IBM_60.json())
# pprint(SMA_IBM_200.json())

RSI = f'https://www.alphavantage.co/query?function=RSI&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey={api_key}'
rsi = requests.get(RSI)
pprint(rsi.json())

MACD = f'https://www.alphavantage.co/query?function=MACD&symbol=IBM&interval=daily&series_type=open&apikey={api_key}'
macd = requests.get(MACD)
pprint(macd.json())