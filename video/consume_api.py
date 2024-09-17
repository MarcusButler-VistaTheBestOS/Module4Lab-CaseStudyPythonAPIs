# Marcus Ed. Butler
# VERSION: 2024-09-17_R0

import requests, json


API = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"

response = requests.get(API)

for data in response.json()['items']:
    print(data['title'])
    print(data['link'], end="\n\n")
