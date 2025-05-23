from scapy.all import ARP, Ether, srp

def scan_network(ip_range)
#Create ARP request packet 
  arp = ARP(pdst=ip range) 
  ether = Ether(dst="ff:ff:ff:ff:ff:ff") 
  packet ether /arp

print(f"Scanning fip_range)Please wait.")

# Send the packet and receive responses 
result = srp(packet, timeout=2, verbose=False)[0]

# Print out the results
devices = []
for sent received in result:
devices.append("ip': received.psrc,macreceived.hwsrc))

print("InAvailable Devices in the Network:")
print("IP" "*18+"MAC") 
print("-"*40)
for device in devices: 
print("f:16) (>".format(device[ ip'],
  device['mac']))
if__name__=="__main__"
target_ip input("Enter the IP rangee (egg.192.168-1.0/24):
scan_network(target_ip)
 
