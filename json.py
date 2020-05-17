import requests

city = input("Enter city name: ")

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=" + city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
jsondata = response.json()
print (jsondata['main']['temp'])

print (jsondata)
print (type(jsondata))
print (jsondata.keys())
print (jsondata.values())
print (len(jsondata.items()))
for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
