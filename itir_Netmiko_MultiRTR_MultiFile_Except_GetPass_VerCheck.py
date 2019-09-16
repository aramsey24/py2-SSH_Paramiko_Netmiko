 #this script runs different configs on multiple devices based on checking the IOS versions. 
 #it incorporates getpass, config files for devices and device file for IP addresses.
 #additional validation commands such as "sh run", "show clock", "sh ip route", etc.. can be included as well. 
 
 
 
 #!/usr/bin/env python
 
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
 
username = raw_input('Enter your SSH username: ')
password = getpass()
 
with open('mgmt_file') as f:
    commands_list_mgmt = f.read().splitlines()
 
with open('r2_file') as f:
    commands_list_r2 = f.read().splitlines()
 
with open('devices_file') as f:
    devices_list = f.read().splitlines()
 
for devices in devices_list:
    print('Connecting to device ') + devices
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device, 
        'username': username,
        'password': password
    }
 
    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print ('Authentication failure: ') + ip_address_of_device
        continue
    except (NetMikoTimeoutException):
        print ('Timeout to device: ') + ip_address_of_device
        continue
    except (EOFError):
        print('End of file while attempting device ') + ip_address_of_device
        continue
    except (SSHException):
        print('SSH Issue. Are you sure SSH is enabled? ') + ip_address_of_device
        continue
    except Exception as unknown_error:
        print('Some other error: ') + str(unknown_error)
        continue
 
    # Types of devices
    list_versions = ['I86BI_LINUXL2-IPBASEK9-M', 
                     'C7200-ADVENTERPRISEK9-M'
                     ]
 
    # Check software versions
    for software_ver in list_versions:
        print('Checking for ') + software_ver
        output_version = net_connect.send_command('show version')
        int_version = 0 # Reset integer value
        int_version = output_version.find(software_ver) # Check software version
        if int_version > 0:
            print ('Software version found: ') + software_ver
            break
        else:
            print ('Did not find ') + software_ver
 
    if software_ver == 'I86BI_LINUXL2-IPBASEK9-M':
        print ('Running ') + software_ver + ' commands'
        output = net_connect.send_config_set(commands_list_mgmt)
    elif software_ver == 'C7200-ADVENTERPRISEK9-M':
        print('Running ') + software_ver + ' commands'
        output = net_connect.send_config_set(commands_list_r2)
  
    print output 