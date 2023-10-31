from netmiko import ConnectHandler


#Detalhes do equipamento
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.100',
    'username': 'cisco',
    'password': 'cisco',
    'port' : 22, #porta default do ssh
    'secret': '', #opcional em caso de um enable secret
    'verbose': True #opcional, definido como true para logs detalhadas
}

#criando a conexão
connection = ConnectHandler(**device)

#executando o comando e retornando a saida
#output é uma variavel que está sendo armazenado o "connection" + função e depois o comando desejado
#use_textfsm=true (ele transforma o comando em uma lista json)
output = connection.send_command('Show ip int brief', use_textfsm =True)

#encerrando a conexão
connection.disconnect()

#mostrando o comando na tela
print(output)

#printando o entry in output
#for entry in output:
   # print(entry)


