import requests
import json

WEBEX_API_URL = 'https://webexapis.com/v1/messages'
WEBEX_ACCESS_TOKEN = 'NTk0NTlhYzYtMDQxMi00ZDExLTk3ODUtMmY2YTIzYThlNzY5YzhmMGRhNDItZjQ2_PF84_519c9506-0f94-4934-a46e-6b7d4f3e98a6'


httpHeaders = {'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}'}
queryParams = {'sortBy': 'lastactivity', 'max': '1'}

body = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vNDY4YTAwMDUtNmMxNy0zZDJmLWI5YTItNjlhN2Q1NjYzYzc0', 'text':'Quem está te respondendo é o robo, ele determina as regras'}

response = requests.post(url=WEBEX_API_URL, headers=httpHeaders, json=body)

print(response.status_code)
print(json.dumps(response.json(), indent=2))

