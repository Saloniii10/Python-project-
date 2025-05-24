 import socket
 import concurrent.futures 
 import sys
 
 RED -"I033[91m"
 GREEN "I033[92m"
 RESET = \033[0m"
def format_port_results(results):

 formatted results = "Port Scan Results:\n"               
formatted_results+="(:<8)f:<15)f:<10]\n".format("Port", "Service" "Status")
 formatted results 85 + "\n" +E 
for port, service, banner, status in results: 
if status:
     formatted results += f"(REDport:<8) fservice:<15> ('Open': <10H(RESETH\n"
 if banner:
      banner_lines = banner-split("In')
       for line in banner_lines: 
     formatted results += F"IGREEN)('":<8)/line)fRESET)\n"
   return formatted results

def get_banner(sock): 
try: 
sock.settimeout(1) 
banner = sock.recv(1024).decode().strip()
 return banner
 except: 
       return ""
 def scan_port(target_ip, port):
      try: 
         sock = socket.socket(socket.AF_INET,                                                                                    socet.SOCKET_STREAM) 
sock.settimeout(1) result = sock connect_ex((target_ip, port))
 if result == 0:
 try: 
    service = socket.getservbyport(port, 'tcp') except:
     service = Unknown banner = get_banner(sock)      return port, service, banner, True 
    else: 
     return port, "" E False 
  except:
     return port, False
      finally:  
        sock.close()
 def port_scan(target_host, start_ port, end_ port): target_ip socket.gethostbyname(target_host) print(f"Starting scan on host{target_ip}")

results = [] with concurrent. futures.ThreadPoolExecutor(max_workers=400) as executor:
 futures = fexecutor.submit(scan_port, target_ip, port): port for port in range(start_port) 
total ports = end_port start_port + 1
 for i in rang in enumerate(concurrent.futures.as_completed(futures), start=1)
 port, service, banner, status future.result() results.append((port, service, banner, status)) sys.stdout.write(f"IrProggress: fi]/total_ports ports scanned") 
sys.stdout.flush()
 
sys.stdout.write("In") print(format_port_results(results))
 
if__name__=="__main__" . 
target_host = input("Enter your target ip: ") start_port = int(input("Enter the start port: ")) end_port = int(input("Enter end port: "))
 port_scan(target_host, start_port, end_port)
