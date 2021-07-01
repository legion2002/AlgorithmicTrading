import numpy as np
import pandas as pd
import math
import requests



url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"q":"INFY","region":"IN"}

headers = {
    'x-rapidapi-key': "22e7a7e69fmsh0d29b7ae8ab3e16p1cb1e4jsn716165fab254",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

print(response)

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

querystring = {"symbol":"INFY","region":"IN"}

headers = {
    'x-rapidapi-key': "22e7a7e69fmsh0d29b7ae8ab3e16p1cb1e4jsn716165fab254",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

querystring = {"region":"IN","symbols":"INFY"}

headers = {
    'x-rapidapi-key': "22e7a7e69fmsh0d29b7ae8ab3e16p1cb1e4jsn716165fab254",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)