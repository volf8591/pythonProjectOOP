# pip install requests
import requests
import json

response = requests.get('https://api.sampleapis.com/coffee/hot')
cofe_data = json.loads(response.text)

for num, data in enumerate(cofe_data):
    print(f'{num}. {cofe_data}')



