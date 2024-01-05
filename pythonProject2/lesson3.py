import requests
import json

response = requests.get('https://www.kufar.by/l/mebel')
mebel_data = response.text
print(mebel_data)
data = mebel_data.split('titl')
print()
