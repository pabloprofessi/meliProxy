import os
import sys

portAmount = 20
startingPort = 8080

ports = range( startingPort , startingPort + portAmount )

for port in ports:
   if sys.argv[1] == "kill":
      os.system("sudo fuser -k " + str(port) + "/tcp")	
   elif sys.argv[1] == "run":
      os.system("python proxyPablo.py " + str(port) + "&")
   elif sys.argv[1] == "reset":
      os.system("sudo fuser -k " + str(port) + "/tcp")	
      os.system("python proxyPablo.py " + str(port) + "&")