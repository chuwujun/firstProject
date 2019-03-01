#! /usr/bin/env python3

import sys
import socket
import re

try:
    if len(sys.argv) != 5:
        raise Exception
    for arg in sys.argv:
        if arg=='--host':
            ip=sys.argv[sys.argv.index(arg)+1]
        if arg=='--port':
            ports=sys.argv[sys.argv.index(arg)+1]
    IPRegex=re.compile(r'^\d+\.\d+\.\d+\.\d+$')
    if IPRegex.match(ip)==None:
        raise Exception
except Exception:
    print("Parameter Error")
    sys.exit()

def scan_port(ip,ports):
    if ports.find('-')!=-1:
        start,end=ports.split('-')
        start,end=int(start),int(end)+1
        list1=range(start,end)
    else:
        list1=[]
        list1.append(int(ports))

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    for one in list1:
        result=s.connect_ex((ip,one))
        if result == 0:
            print(str(one)+" open")
        else:
            print(str(one)+" closed")

scan_port(ip,ports)
