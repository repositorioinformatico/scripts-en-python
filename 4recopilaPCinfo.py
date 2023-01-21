#script that displays public info about your IP, network, geolocation, hardware, etc.
#wrote this just for practice writing python3 scripts
#python3 systemInfo.py


import socket
from urllib.request import urlopen
import re
import json
import sys, getopt
import psutil
import platform
from datetime import datetime
import time
import argparse

#adds CLI usage for -h or --help
msg = "Usage: python3 systemInfo.py"
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description = msg + "\n-----" + "\n\n\n\n\n This script prints information about your machine and network.") 
parser.parse_args() 


#get hostname
hostname = socket.gethostname()

#get IP address  
IPAddr = socket.gethostbyname(hostname)

print("="*30, "IP Information", "="*30)

#prints hostname  
print("Your Computer Name is: " + hostname)

#prints IP address   
print("Your Internal IP Address is: " + IPAddr)

def public_ip():
    read_res = urlopen("http://ipecho.net/plain").read()
    return read_res.decode("utf-8") 
 
if __name__ == "__main__":
    print("Getting public IP...")
    print("Public IP: {} ".format(public_ip(), ))


#gets geo info
url = "http://ipinfo.io/json"
#open url
response = urlopen(url)
#load json response data
data = json.load(response)
 
#json response data
IP=data["ip"]
org=data["org"]
city = data["city"]
country=data["country"]
region=data["region"]

#print line for better spacing
print()
time.sleep(2)


print("Printing your geolocation information")
print("="*30, "Geolocation Information", "="*30)

#Prints IP, region, country, city, org response data
print("IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}".format(org,region,country,city,IP))

#print line for better spacing
print()

time.sleep(2)

print("Printing your system details \n ")
time.sleep(2)
print("="*30, "System Information", "="*30)


#prints general system info
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

#print how long since computer boot
print("="*30, "Boot Time", "="*30)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")


#print CPU cores on current machine
print("="*30, "CPU Info", "="*30)
# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

time.sleep(2)

print()

print("Printing your network interface details \n ")
print("="*30, "Network Interfaces", "="*30)

time.sleep(2)

#prints network interface info
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
