import xmltodict
with open('networking_config.xml', 'r') as file:
    data = xmltodict.parse(file.read())
for router in data['network']['router']:
    router_name = router['hostname']
    for interface in router['interfaces']['interface']:
        iface_name = interface['name']
        ip = interface['ip_address']
        print(f"{router_name}, Interface {iface_name} has IP: {ip}")