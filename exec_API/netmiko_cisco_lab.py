from netmiko import ConnectHandler
import textfsm

# Carregar o modelo TextFSM
with open("template.txt", 'r') as template_file:
    template = textfsm.TextFSM(template_file)

# Detalhes do equipamento
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.100',
    'username': 'cisco',
    'password': 'cisco',
    'port' : 22, # Porta padrão do SSH
    'secret': '', # Opcional, em caso de um "enable secret"
    'verbose': True # Opcional, definido como True para logs detalhados
}

# Criando a conexão
connection = ConnectHandler(**device)

# Executando o comando e obtendo a saída
output = connection.send_command('show ip int brief')

# Usando o modelo TextFSM para analisar a saída
parsed_results = template.ParseText(output)

# Encerrando a conexão
connection.disconnect()

# Mostrando os resultados analisados
for result in parsed_results:
    print(result)
