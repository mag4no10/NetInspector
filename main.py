#!/usr/bin/env python

from pyfiglet import figlet_format
import sys
import socket
import datetime
import os
import time
import subprocess
import argparse
import numpy as np

def printBanner():
    banner = figlet_format("NPSCANNER", font="slant", width=300)
    print(banner)

def printHeaders():
    current_date = datetime.datetime.now()
    print("Starting NP scanner 1.0 at ", end="")
    print(str(current_date.hour) + ":" + str(current_date.minute) + ":" + str(current_date.second) + " WET")

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

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Network Post Scanner")
    parser.add_argument("dest", help="Host to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65535 (all ports)")
    args = parser.parse_args()
    ip, ports = args.dest ,args.port_range
    try:
        printBanner()
        printHeaders()
        target, host_latency = getHostname(ip)
        printOnline(target,host_latency)
        open_ports = scanPorts(target,ports)
        printPorts(open_ports)
    
    except KeyboardInterrupt:
        sigint()