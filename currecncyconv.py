import requests

url = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=07ca862e0b339dd56245"

response = requests.get(url)
data = response.json()['USD_INR']
a = int(input("Enter usd => "))
print(a*data)