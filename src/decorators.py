from loose_functions import *
from operational_functions import *

from colorama import Fore, init, deinit
import sys

banner1 = """                                                          
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠒⠒⠦⣄⡀
⠀⠀⠀⠀⠀⢀⣤⣶⡾⠿⠿⠿⠿⣿⣿⣶⣦⣄⠙⠷⣤⡀
⠀⠀⠀⣠⡾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣷⣄⠘⢿⡄
⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠠⢄⡀⠈⢿⣿⣧⠈⢿⡄
⢀⠏⠀⠀⠀⢀⠄⣀⣴⣾⠿⠛⠛⠛⠷⣦⡙⢦⠀⢻⣿⡆⠘⡇
⠀⠀⠀⠀⡐⢁⣴⡿⠋⢀⠠⣠⠤⠒⠲⡜⣧⢸⠄⢸⣿⡇⠀⡇
⠀⠀⠀⡼⠀⣾⡿⠁⣠⢃⡞⢁⢔⣆⠔⣰⠏⡼⠀⣸⣿⠃⢸⠃               
⠀⠀⢰⡇⢸⣿⡇⠀⡇⢸⡇⣇⣀⣠⠔⠫⠊⠀⣰⣿⠏⡠⠃⠀⠀⢀
⠀⠀⢸⡇⠸⣿⣷⠀⢳⡈⢿⣦⣀⣀⣀⣠⣴⣾⠟⠁⠀⠀⠀⠀⢀⡎
⠀⠀⠘⣷⠀⢻⣿⣧⠀⠙⠢⠌⢉⣛⠛⠋⠉⠀⠀⠀⠀⠀⠀⣠⠎
⠀⠀⠀⠹⣧⡀⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠃
⠀⠀⠀⠀⠈⠻⣤⡈⠻⢿⣿⣷⣦⣤⣤⣤⣤⣤⣴⡾⠛⠉
⠀⠀⠀⠀⠀⠀⠈⠙⠶⢤⣈⣉⠛⠛⠛⠛⠋⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉
"""
banner2 = r"""
          _   _        _    _____                                 _               
      | \ | |      | |  |_   _|                               | |
     |  \| |  ___ | |_   | |   _ __   ___  _ __    ___   ___ | |_  ___   _ __ 
    | . ` | / _ \| __|  | |  | '_ \ / __|| '_ \  / _ \ / __|| __|/ _ \ | '__|
    | |\  ||  __/| |_  _| |_ | | | |\__ \| |_) ||  __/| (__ | |_| (_) || |
    |_| \_| \___| \__||_____||_| |_||___/| .__/  \___| \___| \__|\___/ |_|
                          | |      
                                       |_|
"""
banner3 = r"""⠀⠀⢸⡇⠸⣿⣷⠀⢳⡈⢿⣦⣀⣀⣀⣠⣴⣾⠟⠁⠀⠀⠀⠀⢀⡎
⠀⠀⠘⣷⠀⢻⣿⣧⠀⠙⠢⠌⢉⣛⠛⠋⠉⠀⠀⠀⠀⠀⠀⣠⠎
⠀⠀⠀⠹⣧⡀⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠃                        [Coded by mag4no10]         [v1.0]
⠀⠀⠀⠀⠈⠻⣤⡈⠻⢿⣿⣷⣦⣤⣤⣤⣤⣤⣴⡾⠛⠉
⠀⠀⠀⠀⠀⠀⠈⠙⠶⢤⣈⣉⠛⠛⠛⠛⠋⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉"""

init()
def printBanner():
    spacer = " " * 5
    for a,b in zip(banner1.splitlines(), banner2.splitlines()):
        print(f'{a}{spacer}{b}')
    print(Fore.BLUE + banner3 + "\n\n")
    colorReset()

def printOptions():
    print("\n\n")
    print(Fore.RED + "[", end="")
    print(Fore.LIGHTMAGENTA_EX + "01", end="")
    print(Fore.RED + "]", end="")
    print(Fore.RESET + "  Operating System Information")
    print(Fore.RED + "[", end="")
    print(Fore.LIGHTMAGENTA_EX + "02", end="")
    print(Fore.RED + "]")
    print(Fore.RED + "[", end="")
    print(Fore.LIGHTMAGENTA_EX + "03", end="")
    print(Fore.RED + "]")
    print(Fore.RED + "[", end="")
    print(Fore.LIGHTMAGENTA_EX + "04", end="")
    print(Fore.RED + "]")
    print(Fore.RED + "[", end="")
    print(Fore.LIGHTMAGENTA_EX + "05", end="")
    print(Fore.RED + "]")
    print(Fore.RED + "[", end="")
    print(Fore.LIGHTMAGENTA_EX + "06", end="")
    print(Fore.RED + "]")
    print(Fore.RED + "[", end="")
    print(Fore.LIGHTMAGENTA_EX + "07", end="")
    print(Fore.RED + "]")
    print(Fore.RED + "\n[", end="")
    print(Fore.LIGHTMAGENTA_EX + "00", end="")
    print(Fore.RED + "]", end="")
    print(Fore.RESET + "  exit")
    colorReset()

def printQuest():
    newLine(1)
    print(Fore.RED + "[", end="")
    print(Fore.LIGHTMAGENTA_EX + "~", end="")
    print(Fore.RED + "]", end="")
    colorReset()
    inp = input(" Choose an option: ")
    newLine(1)
    return inp

def optionChecker(option):
    if (option == "00"):
        exitProgram()  
    clear()
    printBanner()
    match option:
        case "01":
            osInfo()

        case _:
            print("Not a valid option, try again")

deinit()