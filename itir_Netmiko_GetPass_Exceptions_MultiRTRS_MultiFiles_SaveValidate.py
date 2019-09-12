 
 #the script imports getpass and exception modules from netmiko and paramiko. 
 #the exceptions handle timeouts, authentication failures and ssh issues. 
 #the script makes changes to multiple devices with their own respective cofigs. 
 
 
 #!/usr/bin/env python

 


#for r1

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException




username = raw_input('enter your username: ')
password = getpass()


with open('r1_file') as f:
    commands_list = f.read().splitlines()

devices_list = ['r1']

for devices in devices_list:
    print('connecting to device ') + devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': "192.168.122.213",
        'username': username, 
        'password': password
    }
    
    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print 'authentication failure ' + devices
        continue
    except (NetMikoTimeoutException):
        print 'Timeout to device: ' + devices
        continue
    except (EOFError):
        print 'end of file while attempting device ' + devices
        continue
    except (SSHException):
        print 'SSH issue. Are you sure SSH is enabled? ' + devices
        continue
    
    output = net_connect.send_config_set(commands_list)
    output += net_connect.send_command('write me')
    output += net_connect.send_command('show ip route')
    output += net_connect.send_command('show ip int brief')
    output += net_connect.send_command('show run')
    print (output)


#for mgmt_switch

with open('mgmt_file') as f:
    commands_list = f.read().splitlines()

devices_list = ['mgmt_switch']

for devices in devices_list:
    print('connecting to device ') + devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': "192.168.122.26",
        'username': username, 
        'password': password
    }
    
    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print 'authentication failure ' + devices
        continue
    except (NetMikoTimeoutException):
        print 'Timeout to device: ' + devices
        continue
    except (EOFError):
        print 'end of file while attempting device ' + devices
        continue
    except (SSHException):
        print 'SSH issue. Are you sure SSH is enabled? ' + devices
        continue
    
    output = net_connect.send_config_set(commands_list)
    output += net_connect.send_command('write me')
    output += net_connect.send_command('show ip route')
    output += net_connect.send_command('show ip int brief')
    output += net_connect.send_command('show run')
    print (output)





with open('s1_file') as f:
    commands_list = f.read().splitlines()

devices_list = ['s1_switch']

for devices in devices_list:
    print('connecting to device ') + devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': "192.168.122.27",
        'username': username, 
        'password': password
    }
    
    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print 'authentication failure ' + devices
        continue
    except (NetMikoTimeoutException):
        print 'Timeout to device: ' + devices
        continue
    except (EOFError):
        print 'end of file while attempting device ' + devices
        continue
    except (SSHException):
        print 'SSH issue. Are you sure SSH is enabled? ' + devices
        continue


    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_list)
    output += net_connect.send_command('write me')
    output += net_connect.send_command('show ip route')
    output += net_connect.send_command('show ip int brief')
    output += net_connect.send_command('show run')
    print (output)