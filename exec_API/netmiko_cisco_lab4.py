#importando a biblioteca netmiko
from netmiko import ConnectHandler
import textfsm
import json

#descrevendo as caracteristicas do device
device = {
    'device_type': 'cisco_ios',
    'ip': 'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876',
    'port': 22, #porta default ssh
    'secret': '', #em caso de enable secret
    'verbose': True #opcional em caso de logs no terminal
}

#abrindo uma conexão com o dispositivo com as caracteristicas do device definida em "device"
connection = ConnectHandler(**device)

#emitindo uma saida de configuração com a função "send_command" e o comando a ser aplicado é "show ip int brief"
#usando o "textfsm" para sair uma lista em json
output = connection.send_command('Show ip int brief', use_textfsm=True)

print(output) 

#fechando a conexão com o device
connection.disconnect()


#Agora, vamos procurar a interface específica e exibir detalhes relevantes:
target_interface = "Loopback1"

# é uma forma de informar de validar se a interface está criada, essa variável já começa como False.
# essa variavel vai ser chamada abaixo.
interface_found = False

#esse código vai percorrer a lista json fornecido pelo resultado de output
#se intf for igual a interface informada em target_interface ele vai exibir as informações solicitadas
# interface_found vai ficar true pq a interface que foi relatada em target_interface existe
# se a interface não for localizada na saida de output ele vai exibir a informação de if not interface_found.
for entry in output:
    if entry['intf'] == target_interface:
        interface_found = True
        print(f"interface name:{entry['intf']}\nIP Address: {entry['ipaddr']}\nStatus: {entry['status']}\n Protocol: {entry['proto']}\n")
        break
    if not interface_found:
        print(f"interface {target_interface} não foi criada")
    