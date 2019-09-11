#this script uses paramiko/netmiko to configure multiple devices with the same type of configuration. 
#this script uses seperate file named "l2_config" to call the configuration being applied to all switches. 
#David Bombal:Python for Network Engineers with GNS3 (Part 14) - Netmiko, SSH, Python Cisco switches

#https://www.youtube.com/watch?v=gEVFRBnjpS4



#configuration for file "l2_config"
vlan 2
int range Gi2/0 - 1
switchport mode access
switchport access vlan 2
int range g2/2 - 3
switchport trunk encap dot1q
switchport mode trunk
 no negotiation auto
switchport trunk allowed vlan 1,2



#!/usr/bin/env python

from netmiko import ConnectHandler

ios_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.26',
    'username': 'cisco',
    'password': 'cisco',
}

ios_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.27',
    'username': 'cisco',
    'password': 'cisco',
}

ios_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.28',
    'username': 'cisco',
    'password': 'cisco',
}

ios_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.29',
    'username': 'cisco',
    'password': 'cisco',
}


with open('l2_config') as f:
    lines = f.read().splitlines()
    print lines

all_devices =[ios_s4, ios_s3, ios_s2, ios_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output

