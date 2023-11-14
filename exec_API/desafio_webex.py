import requests
import json

WEBEX_API_URL = 'https://webexapis.com/v1/rooms'
WEBEX_ACCESS_TOKEN = 'NTk0NTlhYzYtMDQxMi00ZDExLTk3ODUtMmY2YTIzYThlNzY5YzhmMGRhNDItZjQ2_PF84_519c9506-0f94-4934-a46e-6b7d4f3e98a6'

httpHeaders = {'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}'}
queryParams = {'sortBy': 'lastactivity', 'max': '6'}

response = requests.get(url=WEBEX_API_URL, headers=httpHeaders, params=queryParams)


if response.status_code == 200:
    print( response.status_code )
    print(json.dumps(response.json(), indent=2))
    print(response.json()['items'][0]['id'])
else:
    print("solicitação não encontrada") 