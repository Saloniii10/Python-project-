 import socket
 import concurrent.futures 
 import sys
 
 RED -"I033[91m"
 GREEN "I033[92m"
 RESET = \033[0m"
def format_port_results(results):

 formatted results = "Port Scan Results:\n"               
 formatted_results+="(:<8)f:<15)f:<10]\n".format("Port", "Service" "Status") formatted results 85 + "In" +E for port, service, banner, status in results: if status: formatted results += f"(REDport:<8) fservice:<15> ('Open': <10H(RESETH\n" if banner: banner_lines = banner-split("In') for line in banner_lines: formatted results += F"IGREEN)('":<8)/line)fRESET)\n" return formatted results