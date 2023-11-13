import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Roma, Itália"
dest = "Frascati, Itália"
key = "C0zGyANehea5nxzutNahUkea2vautJQr"  # Substitua pela sua chave MapQuest
url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
json_data = requests.get(url).json()
print(json_data)

for x in json_data:
    print(x)