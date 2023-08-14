#!/usr/bin/env python

from loose_functions import *
from decorators import *

import sys
import socket
import subprocess



def getHostname(ip):
    try:
        target = socket.gethostbyname(ip)
        host_latency = subprocess.check_output("ping -c1 " + ip + " | grep -oP 'time=.*' | grep -o '=.*' | sed 's/^.//'", shell=True);
        return target,host_latency
    except socket.error:
        print("[*] Server is not responding")
        sys.exit(1)

def scanPorts(target,ports):
    try:
        start_port, end_port = ports.split("-")
        start_port, end_port = int(start_port), int(end_port)
        ports = [ p for p in range(start_port, end_port)]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_collection = []
        for port in ports:
            result = s.connect_ex((target,port))
            socket.setdefaulttimeout(1)
            if (result == 0):
                port_collection.append(port)
        s.close()
        return port_collection
    except socket.gaierror:
        print("Host is down")

def printOnline(target, host_latency):
    latency = host_latency.decode()
    latency = latency.strip()
    print("Host ({}) is up with {} \r".format(target,latency))

def printPorts(open_ports):
    print("Ports opened -> " + str(open_ports))

def sigint():
    print("",end="\r")
    print("[*] SIGINT signal detected")
    print("[*] Exiting...")
    sys.exit()

def menu():
    option = 1000
    while (option != "00"):
        clear()
        printBanner()
        printOptions()
        option = printQuest()
        optionChecker(option)

if __name__ == "__main__" :
    try:
        menu()
    except KeyboardInterrupt:
        sigint()