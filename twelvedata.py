import requests

url = "https://twelve-data1.p.rapidapi.com/quote"

querystring = {"symbol":"RELIANCE","interval":"1day","format":"json","outputsize":"30"}

headers = {
    'x-rapidapi-key': "22e7a7e69fmsh0d29b7ae8ab3e16p1cb1e4jsn716165fab254",
    'x-rapidapi-host': "twelve-data1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)