import requests
import json
r = requests.get("http://api.worldbank.org/v2/country/br?format=json")
item = r.json()
#print(item)
for i in item[1]:
  print(i['name'])

