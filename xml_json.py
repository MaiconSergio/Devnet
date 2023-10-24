import xml.etree.ElementTree as ET
import json
tree = ET.parse('networking_config.xml')
root = tree.getroot()

network = {"routers": []}

for router in root.findall('router'):   
    router_data = {
        "id": router.find('id').text,
        "hostname": router.find('hostname').text,
        "interfaces": [
            {
                "name": iface.find('name').text,
                "ip_address": iface.find('ip_address').text,
                "subnet_mask": iface.find('subnet_mask').text
            }
            for iface in router.findall('interfaces/interface')
        ]
    }
    network['routers'].append(router_data)
with open('network_config.json', 'w') as json_file:
    json.dump(network, json_file, indent=4)