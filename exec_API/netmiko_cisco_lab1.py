import textfsm

# Carregar o template
with open("template.txt", 'r') as template_file:
    template = textfsm.TextFSM(template_file)

# Sample command output
command_output = """
Interface              IP-Address      Status     Protocol
FastEthernet0/0        10.0.0.1        up         up      
FastEthernet0/1        unassigned      down       down
"""
parsed_results = template.ParseText(command_output)

# Imprimir resultados analisados
for result in parsed_results:
    print(result)