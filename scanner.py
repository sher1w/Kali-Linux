#!/usr/bin/python3   #  shebang line corrected

import sys          # for command-line arguments
import socket       # for network connections
from datetime import datetime  # to show the start time

# --- DEFINE TARGET ---
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # translates hostname to IPv4
    print("Scanning target: " + target)
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip or hostname>")
    sys.exit()  # Exit early if input is incorrect

# BANNER
print("-" * 50)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
      for port in range(50,85):
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         socket.setdefaulttimeout(1)
         result = s.connect_ex((target,port))
         print("Checking port {}".format(port))
         if result == 0:
           print("Port {} is open".format(port))
         s.close()
except KeyboardInterrupt:
       print("\n Exciting program. ")
       sys.exit()  # This ends the program mmediately


except socket.gaierror:
  print("Hostname could not be resolved ")
  sys.exit()
 
except socket.error:
 print("COuldnt connect to server.")
 sys.exit()

