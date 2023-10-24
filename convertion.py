import xml.etree.ElementTree as ET
import json

# XML data
xml_data = """
<?xml version="1.0" encoding="UTF-8"?>
<network>
  <router>
    <id>R1</id>
    <hostname>Router1</hostname>
    <interfaces>
      <interface>
        <name>eth0</name>
        <ip_address>192.168.1.1</ip_address>
        <subnet_mask>255.255.255.0</subnet_mask>
      </interface>
      <interface>
        <name>eth1</name>
        <ip_address>192.168.2.1</ip_address>
        <subnet_mask>255.255.255.0</subnet_mask>
      </interface>
    </interfaces>
  </router>
  <router>
    <id>R2</id>
    <hostname>Router2</hostname>
    <interfaces>
      <interface>
        <name>eth0</name>
        <ip_address>192.168.3.1</ip_address>
        <subnet_mask>255.255.255.0</subnet_mask>
      </interface>
      <interface>
        <name>eth1</name>
        <ip_address>192.168.4.1</ip_address>
        <subnet_mask>255.255.255.0</subnet_mask>
      </interface>
    </interfaces>
  </router>
</network>
"""

# Parse o XML
root = ET.fromstring(xml_data)

# Converter XML em um dicionário
def xml_to_dict(element):
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        if child_data:
            result[child.tag] = child_data
        else:
            result[child.tag] = child.text
    return result

xml_dict = xml_to_dict(root)

# Converter o dicionário em JSON
json_data = json.dumps(xml_dict, indent=4)

# Imprimir o JSON resultante
print(json_data)
