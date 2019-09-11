#this script shows how to apply different configs on each switch
#for example: core switches will have a particular config
#and access switches will have their specific config. 
#This is done by their own respective files being called in the main script.
#the files are called: There are two core switches: ios_core_s1 & ios_core_s1
#there are two access switches: ios_access_s3 & ios_access_s4



#David Bombal: Python for Network Engineers with GNS3 (Part 15) - Netmiko, SSH, Python Cisco switches
#https://www.youtube.com/watch?v=L_YfSU378yI

#the files being called in loop just contain loopback interfaces and ospf config

#interface loopback 3
#ip address 3.3.3.3 255.255.255.255
#interface loopback 33
#ip address 33.33.33.33 255.255.255.255
#router ospf 1
#network 3.3.3.3 255.255.255.255 area 0
#network 33.33.33.33 255.255.255 area 0
#network 192.168.122.0 255.255.255.0 area 0






#!/usr/bin/env python

from netmiko import ConnectHandler
import time

ios_core_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.26',
    'username': 'cisco',
    'password': 'cisco',
}

ios_core_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.27',
    'username': 'cisco',
    'password': 'cisco',
}

ios_access_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.28',
    'username': 'cisco',
    'password': 'cisco',
}

ios_access_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.29',
    'username': 'cisco',
    'password': 'cisco',
}


ios_access_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.30',
    'username': 'cisco',
    'password': 'cisco',
}



with open('S1_core_config') as f:
    lines = f.read().splitlines()
    print lines

all_devices =[ios_core_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output
    time.sleep(0.5)


with open('S2_core_config') as f:
    lines = f.read().splitlines()
    print lines
    

all_devices =[ios_core_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output
    time.sleep(0.5)

with open('S3_access_config') as f:
    lines = f.read().splitlines()
    print lines

all_devices =[ios_access_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output
    time.sleep(0.5)

with open('S4_access_config') as f:
    lines = f.read().splitlines()
    print lines

all_devices =[ios_access_s4]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output
    time.sleep(0.5)

with open('S5_access_config') as f:
    lines = f.read().splitlines()
    print lines

all_devices =[ios_access_s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output
    time.sleep(0.5)
 
