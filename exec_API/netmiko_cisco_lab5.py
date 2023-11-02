from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.100',
    'username': 'cisco',
    'password': 'cisco',
    'port': 22,
    'secret': '',
    'verbose': False
}


#create a connection
connection = ConnectHandler(**device)
print(f"{connection} conectado")

output = connection.send_command('Show ip int brief')
print(output)
# Loopback Details



# CLI configuration to remove the interface

for x in range(6,11):
    loopback = {
    'int_name': f'loopback{x}'
    }
    
    
    interface_config = [
    f"no interface {loopback['int_name']}",
    
]
    print(f"{loopback} removida com sucesso")
# Send configuration to the device
    output = connection.send_config_set(interface_config)

# Close the connection

connection.disconnect()
# Print the output to confirm deletion

