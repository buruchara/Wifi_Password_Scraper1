# Wifi_Password_Scraper1
Extracting Wi-Fi password From windows machine
The given code is a Python script that performs the following tasks:

Imports the necessary modules: subprocess, os, and io.
Creates a file named "passwords.txt" to store previously connected Wi-Fi passwords.
Executes a Windows command using the subprocess.run() function to export Wi-Fi profiles with clear text passwords.
Retrieves the current directory using os.getcwd().
Searches for Wi-Fi profile files in the current directory that start with "Wi-Fi" and end with ".xml".
Appends the filenames of Wi-Fi profile files that match the criteria to the wifi_files list.
