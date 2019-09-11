#this script configures multiple devices via ssh/paramiko/netmiko. Netmiko provides vendor specific commands
#note: naming the devices is very important here..otherwise you'll see errors in script. I tried just "S1", it didn't work.
#had to specify "ios_s1"
#David Bombal: Python for Network Engineers with GNS3 (Part 13) - Netmiko, SSH, Python Cisco switches
#https://www.youtube.com/watch?v=IQctXVwKboA



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


all_devices = [ios_s1, ios_s2, ios_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print "Creating VLAN " + str(n)
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print output 