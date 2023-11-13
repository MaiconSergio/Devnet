import requests
import sys

# Disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Device details
HOST = 'sandbox-iosxe-recomm-1.cisco.com'
USER = 'developer'
PASS = 'lastorangerestoreball8876'

def main():
    """Retrieve Interface details from the device via RESTCONF."""
    
    # Construct the URL
    url = "https://{h}/restconf/data/ietf-interfaces:interfaces".format(h=HOST)
    
    
    # Headers for the GET request
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }
    
    # Make the GET request
    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
    
    # Print the returned JSON data
    print(response.text)

if __name__ == '__main__':
    main()