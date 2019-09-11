#module for using SSH is paramiko
#additional commands used in ubuntu: 
#note: python is already installed but if it wasn't and it's a fresh isntall of ubuntu then:
#apt-get update
#apt-get install python -y

#so if python is already installed then continue below commands:
#apt-get install build-essential libssl-dev libffi-dev -y
#apt-get install python-pip -y
#apt-get installpython-dev
#pip install cryptography
#pip install --upgrade pip

#David Bombal: Python for Network Engineers with GNS3 (Part 11) - Paramiko, SSH, Python and Cisco
#https://www.youtube.com/watch?v=xd1kI1eq5uw&t=106s

 
#!/usr/bin/env python

import paramiko
import time


ip_address = "192.168.122.26"
username = "cisco"
password = "cisco"



    
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successfull Connection" , ip_address



root@ubuntu:~# 
root@ubuntu:~# cat ./sshconfig.py 
#!/usr/bin/env python

import paramiko
import time


ip_address = "192.168.122.26"
username = "cisco"
password = "cisco"



    
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successfull Connection" , ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("conf t\n")
remote_connection.send("int loopback 0\n")
remote_connection.send("ip address 1.1.1.1 255.255.255.255\n")
remote_connection.send("interface loopback 1\n")
remote_connection.send("ip address 2.2.2.2 255.255.255.255\n")


for n in range (2,21):
    print "Creating VLAN " + str(n)
    remote_connection.send("vlan " + str(n) + "\n")
    remote_connection.send("name Python_VLAN " + str(n) + "\n")
    time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)

output = remote_connection.recv(65535)
print output


ssh_client.close