from code import interact
import socket
import sys 
from datetime import datetime
from unittest import result

print("Hey wellcome to the termble port scanner")
#zitame apo ton xristi na bali to onoma to host poy theli na scannary
remote_server = input("Enter a remote host to scan: ")
#socket.gethostbyname mas emfanizi tin ip toy host poy exei anazitisi o xristis
remote_server_IP = socket.gethostbyname(remote_server)
#print(remote_server_IP)
print("_" * 60)
print("Please wait scanning remote host:" +remote_server)
print("_" * 60)
t1 = datetime.now()
try:   
    for port in range(1,5000): 
    
#                                IPv4            TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remote_server, port))
        if result == 0:
            print("Port{}:     is open".format(port))
            sock.close()
except KeyboardInterrupt:
    print("You press Ctr + C")
    sys.exit()

except socket.gaierror:
    print("Your host name could not resolved.Exit..")
    sys.exit()
except socket.error:
    print("Couldn't connect to server") 
    sys.exit()
t2 = datetime.now()
total = t2 - t1
print('Scan complite in '+total)
