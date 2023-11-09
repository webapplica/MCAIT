import pypaloalto # before you have install this lib : pip install pypaloalto

# Define Palo Alto firewall connection information
host = "ip_of_firewall"
username = "username"
password = "password"

# Connect to the Palo Alto firewall
firewall = pypaloalto.Panorama(host, username, password)

# Get Palo Alto firewall configuration
config = firewall.get_config()

# Save the Palo Alto firewall configuration in a text file
with open("paloalto-config.txt", "w") as f:
    f.write(config)


#Another way to do it using the XML API
#https://blog.networkers.fi/panos-config-backups/

# TIP: you can also using curl
#curl -kG "https://<firewall-ip>/api/?type=export&category=configuration&key=<api_key>" > c:\running-config_%date%.xml
