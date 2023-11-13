import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "C0zGyANehea5nxzutNahUkea2vautJQr"
while True:
  orig = input("Local de partida: ")
  if orig == "quit" or orig == "q":
        print("Você encerrou o programa")
        break
  dest = input("Destino: ")
  if dest == "quit" or orig == "q":
        print("Você encerrou o programa")
        break
  url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
  print("URL: " + (url))
  json_data = requests.get(url).json()
  json_status = json_data["info"]["statuscode"]
  if json_status == 0:
    print("API Status: " + str(json_status) + " = Chamada de rota bem-sucedida.\n")
    print("=============================================")
    print("Direções de " + (orig) + " para " + (dest))
    print("Duração da Viagem: " + (json_data["route"]["formattedTime"]))
    print("Milhas: " + str(json_data["route"]["distance"]))
    print("=============================================")
    
