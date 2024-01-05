import xml.etree.ElementTree as ET
import yaml
tree = ET.parse('networking_config.xml')
root = tree.getroot()

network = {"routers": []}
#comentario novo

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
# Converter os dados em YAML e salvar
with open('networking_config.yaml', 'w') as yaml_file:
    yaml.dump(network, yaml_file, default_flow_style=False)
