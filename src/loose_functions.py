import os
from colorama import Fore
from sys import exit


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def colorReset():
    print(Fore.RESET, end="")

def exitProgram():
    print("[+] Exiting program...")
    exit(0)

def newLine(num):
    for i in range(num): print("\n")
