#importando a biblioteca netmiko
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.100',
    'username': 'cisco',
    'password': 'cisco',
    'port': 22, #porta default ssh
    'secret': '', #em caso de enable secret
    'verbose': True #opcional em caso de logs no terminal
}


connect = ConnectHandler(**device)
print("DEVICE CONECTADO")

# se o equipamento conectar ele vai exibir a mensagem e se não vai exibir outra mensagem

#em um range de 1 a 10 ele vai criar as interfaces conforme informações passadas
for i in range(1, 11):
    loopback = {
        'int_name': f'loopback{i}',
        'description': f' interface teste loopback {i}',
        'ipS': f'182.168.30.{i}',
        'netmask': '255.255.255.255'
}
#essas são as configurações aplicadas dentro do equipamento
    int_config = [  
        f"interface {loopback['int_name']}",
        f"description{loopback['description']}",
        f"ip address {loopback['ipS']} {loopback['netmask']}",
        'no shutdown'
]
#uma função que seta as configurações definidas na variavel apontada (int_config)
    out = connect.send_config_set(int_config)
#Listando as interfaces criadas
    print(f"foi criado a interface {loopback} ")
    print(out)

connect.disconnect()

#PRIMEIRA FORMA DE CRIAR UM LOOP PARA INTERFACES