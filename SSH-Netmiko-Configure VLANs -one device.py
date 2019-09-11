#Paramiko is a Python implementation of the SSH  version 2 protocol and provides both client and server functionality. 
#Now Netmiko is a multi-vendor library that was developed to simplify Paramiko SSH connections to network devices.
#Netmiko recognizes and provides vendor specific commands in its library of commands.
#for more info: https://ktbyers.github.io/netmiko/#installation
#David Bombal youtube lesson:  Python for Network Engineers with GNS3 (Part 12) - Netmiko, SSH, Python and Cisco
#https://www.youtube.com/watch?v=GN8aTXMdycY

#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2  = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.26',
    'username': 'cisco',
    'password': 'cisco',
}


net_connect = ConnectHandler(**iosv_l2)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print output

config_commands = ["int loop 0", "ip address 1.1.1.1 255.255.255.0"]
output = net_connect.send_config_set(config_commands)
print output


for n in range (2,26):
    print'Creating VLAN' + str(n)
    config_commands = [
    'vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output

#I added the save commands below
save_commands = ['end', 'wri me']
output = net_connect.send_config_set(save_commands)
