# Writing a simple algorithm
ip_list = ["198.223.XX.XX", "198.101.xx.xx", "180.64.xx.xx", "192.168.xx.xx", "184.90.xx.xx"]
networks = []

for address in ip_list:
    networks.append(address[0:3])
    
print(networks)