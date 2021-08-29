

#importing librarys#
from colorama import *
import time
import webbrowser
import subprocess
import os

#making variables#
name = input
terminal = input






#setup process#
print(Back.GREEN + Fore.BLACK + Style.DIM + "Welcome to the terminal! Lets get you set up. You can enter a nickname, I will call you whatever you type in.")
name = input("User: ")
print("Hello "+name+"!")
print("You are all set up. You can say 'help' whenever you need to.")
terminal = input(name+(": "))




#all of the possible commands#


if terminal == ("rickroll"):
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    terminal = input(name+(": "))






if terminal == ("print"):
    print_ = input("print"+(": "))
    print(print_)
    print()
    print("printed.")
    terminal = input(name+(": "))








if terminal == ("calculator"):
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    terminal = input(name+(": "))







if terminal == ("steam"):
    subprocess.Popen("C:\\Program Files (x86)\Steam\steam.exe")
    terminal = input(name(":"))




























