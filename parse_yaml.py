import yaml

with open('networking_config.yaml', 'r') as file:
    data = yaml.safe_load(file)
for router in data['routers']:
    router_name = router['hostname']
    for interface in router['interfaces']: 
        iface_name = interface['name']
        ip = interface['ip_address']
        print(f"{router_name}, Interface {iface_name} has IP: {ip}")