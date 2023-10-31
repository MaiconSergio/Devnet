from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.100',
    'username': 'cisco',
    'password': 'cisco',
    'port': 22,          # Default SSH port
    'secret': '',        # Optional, in case of enable password
    'verbose': True      # Optional, set to True for verbose logs
}

# Create a connection
connection = ConnectHandler(**device)

# Create 10 loopback interfaces
int_loopback = 0
ip_range = '192.168.25'

#SEGUNDA FORMA DE CRIAR UM LOOP PARA CRIAÇÃO DE INTERFACES

while int_loopback <= 15:
    interface_config = [
        f"interface loopback {int_loopback}",
        f"description {int_loopback}",
        f"ip address {ip_range}.{int_loopback} 255.255.255.255",
        f"no shutdown",
          
    ]
    int_loopback +=1
    # Send configuration to the device for each loopback
    output = connection.send_config_set(interface_config)

    # Print the output to verify the interface configuration
    print(f"The following configuration was sent for str({int_loopback}):")
    print(output)

# Close the connection
connection.disconnect()
