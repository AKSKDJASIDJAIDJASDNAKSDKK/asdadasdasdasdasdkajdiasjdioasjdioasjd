import subprocess
import os
from colorama import Fore, Back, Style
from sys import platform
import time
import requests
from discord_webhook import DiscordWebhook
import shutil 
import sqlite3 
import zipfile 
import json 
import base64 
import psutil 
import pyautogui
from win32crypt import CryptUnprotectData
from re import findall
from Crypto.Cipher import AES
import socket
import sys

#--------------------------------#

import os
import time, sys, time, os
try:
    import requests
    from colorama import Fore, init
    from dhooks import Webhook
except (ModuleNotFoundError):
    os.system('pip install requests colorama')

from colorama import Fore, init
import base64
init(convert=True)

# grabber imports
import httpx
import os
import json 
import base64
from re import findall
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
os.system(f'cls & mode 85,20 & title Numb Tools V2')

#--------------------------------#


  ###################
  #    COLORS       #
  ###################


black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
brown = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
light_gray = "\033[0;37m"
dark_gray = "\033[1;30m"
light_red = "\033[1;31m"
light_green = "\033[1;32m"
yellow = "\033[1;33m"
light_blue = "\033[1;34m"
light_purple = "\033[1;35m"
light_cyan = "\033[1;36m"
light_white = "\033[1;37m"
bold = "\033[1m"
faint = "\033[2m"
italic = "\033[3m"
underline = "\033[4m"
blink = "\033[5m"
negative = "\033[7m"
crossed = "\033[9m"
end = "\033[0m"

hn = socket.gethostname()
r = requests.get('https://pastebin.com/raw/bx9PyGYf')

try:
    if hn in r.text:
        pass
    else:
        os.system("title Numb Tools V2 /// Checking Database...")
        print("[/] Checking database")
        time.sleep(1)
        os.system("cls")
        print("[\] Checking database")
        time.sleep(1)
        os.system("cls")
        print("[+] Checking database")
        time.sleep(1)
        os.system("cls")
        print("[-] Checking database")
        time.sleep(3)
        os.system("title Numb Tools V2 /// PC Not Found")
        print("[X] PC Is Not in database")
        time.sleep(1)
        print(f'[=] Your PC Id: {hn}') 
        time.sleep(5)
        os._exit()
except:
    print("[-] Failed to connect to database")
    time.sleep(5)
    os._exit()


os.system("title Numb Tools V2 /// Checking Database...")
print("[/] Checking database")
time.sleep(1)
os.system("cls")
print("[\] Checking database")
time.sleep(1)
os.system("cls")
print("[+] Checking database")
time.sleep(1)
os.system("cls")
print("[-] Checking database")
time.sleep(3)
os.system("title Numb Tools V2 /// PC Found!")
print("[+] PC Authenticated")
time.sleep(3)
os.system("cls")


 #################
 # LOADING SYSTEM #
 #################


os.system("title Numb Tools V2 /// Hub loading...")
print("""

\033[0;35m888                 \033[0;34m           888 \033[1;35md8b                   
\033[0;35m888                 \033[0;34m           888 \033[1;35mY8P                   
\033[0;35m888                \033[0;34m            888 \033[1;35m                       
\033[0;35m888      .d88b.   \033[0;34m8888b.   .d88888 \033[1;35m888 88888b.   .d88b.      
\033[0;35m888     d88""88b  \033[0;34m   "88b d88" 888 \033[1;35m888 888 "88b d88P"88b 
\033[0;35m888     888  888 .\033[0;34md888888 888  888 \033[1;35m888 888  888 888  888 
\033[0;35m888     Y88..88P \033[0;34m888  888 Y88b 888 \033[1;35m888 888  888 Y88b 888 
\033[0;35m88888888 "Y88P"  \033[0;34m"Y888888  "Y88888 \033[1;35m888 888  888  "Y88888 
\033[0;35m                                   \033[1;35m                  888 
\033[0;35m                                   \033[1;35m            Y8b d88P 
\033[0;35m                                   \033[1;35m             "Y88P\033[0m

          \033[1;30m[+] I'm redirecting you to the hub...""")

time.sleep(1)
os.system("cls")


    ############################
    # ANIMATION SYSTEM LOADING #
    ############################

print("""

\033[0;35m888                 \033[0;34m           888 \033[1;35md8b                   
\033[0;35m888                 \033[0;34m           888 \033[1;35mY8P                   
\033[0;35m888                \033[0;34m            888 \033[1;35m                       
\033[0;35m888      .d88b.   \033[0;34m8888b.   .d88888 \033[1;35m888 88888b.   .d88b.      
\033[0;35m888     d88""88b  \033[0;34m   "88b d88" 888 \033[1;35m888 888 "88b d88P"88b 
\033[0;35m888     888  888 .\033[0;34md888888 888  888 \033[1;35m888 888  888 888  888 
\033[0;35m888     Y88..88P \033[0;34m888  888 Y88b 888 \033[1;35m888 888  888 Y88b 888 
\033[0;35m88888888 "Y88P"  \033[0;34m"Y888888  "Y88888 \033[1;35m888 888  888  "Y88888 
\033[0;35m                                   \033[1;35m                  888 
\033[0;35m                                   \033[1;35m            Y8b d88P 
\033[0;35m                                   \033[1;35m             "Y88P\033[0m

          \033[1;30m[+] I'm redirecting you to the hub...""")

time.sleep(1)
os.system("cls")

print("""

\033[0;35m888                 \033[0;34m           888 \033[1;35md8b                   
\033[0;35m888                 \033[0;34m           888 \033[1;35mY8P                   
\033[0;35m888                \033[0;34m            888 \033[1;35m                       
\033[0;35m888      .d88b.   \033[0;34m8888b.   .d88888 \033[1;35m888 88888b.   .d88b.      
\033[0;35m888     d88""88b  \033[0;34m   "88b d88" 888 \033[1;35m888 888 "88b d88P"88b 
\033[0;35m888     888  888 .\033[0;34md888888 888  888 \033[1;35m888 888  888 888  888 
\033[0;35m888     Y88..88P \033[0;34m888  888 Y88b 888 \033[1;35m888 888  888 Y88b 888 
\033[0;35m88888888 "Y88P"  \033[0;34m"Y888888  "Y88888 \033[1;35m888 888  888  "Y88888 
\033[0;35m                                   \033[1;35m                  888 
\033[0;35m                                   \033[1;35m            Y8b d88P 
\033[0;35m                                   \033[1;35m             "Y88P\033[0m

          \033[1;30m[-] I'm redirecting you to the hub...""")

time.sleep(1)
os.system("cls")


print("""

\033[0;35m888                 \033[0;34m           888 \033[1;35md8b                   
\033[0;35m888                 \033[0;34m           888 \033[1;35mY8P                   
\033[0;35m888                \033[0;34m            888 \033[1;35m                       
\033[0;35m888      .d88b.   \033[0;34m8888b.   .d88888 \033[1;35m888 88888b.   .d88b.      
\033[0;35m888     d88""88b  \033[0;34m   "88b d88" 888 \033[1;35m888 888 "88b d88P"88b 
\033[0;35m888     888  888 .\033[0;34md888888 888  888 \033[1;35m888 888  888 888  888 
\033[0;35m888     Y88..88P \033[0;34m888  888 Y88b 888 \033[1;35m888 888  888 Y88b 888 
\033[0;35m88888888 "Y88P"  \033[0;34m"Y888888  "Y88888 \033[1;35m888 888  888  "Y88888 
\033[0;35m                                   \033[1;35m                  888 
\033[0;35m                                   \033[1;35m            Y8b d88P 
\033[0;35m                                   \033[1;35m             "Y88P\033[0m

          \033[1;30m[-] I'm redirecting you to the hub...""")

time.sleep(1)
os.system("cls")

print("""

\033[0;35m888                 \033[0;34m           888 \033[1;35md8b                   
\033[0;35m888                 \033[0;34m           888 \033[1;35mY8P                   
\033[0;35m888                \033[0;34m            888 \033[1;35m                       
\033[0;35m888      .d88b.   \033[0;34m8888b.   .d88888 \033[1;35m888 88888b.   .d88b.      
\033[0;35m888     d88""88b  \033[0;34m   "88b d88" 888 \033[1;35m888 888 "88b d88P"88b 
\033[0;35m888     888  888 .\033[0;34md888888 888  888 \033[1;35m888 888  888 888  888 
\033[0;35m888     Y88..88P \033[0;34m888  888 Y88b 888 \033[1;35m888 888  888 Y88b 888 
\033[0;35m88888888 "Y88P"  \033[0;34m"Y888888  "Y88888 \033[1;35m888 888  888  "Y88888 
\033[0;35m                                   \033[1;35m                  888 
\033[0;35m                                   \033[1;35m            Y8b d88P 
\033[0;35m                                   \033[1;35m             "Y88P\033[0m

          \033[1;30m[/] I'm redirecting you to the hub...""")

time.sleep(1)
os.system("cls")

print("""

\033[0;35m888                 \033[0;34m           888 \033[1;35md8b                   
\033[0;35m888                 \033[0;34m           888 \033[1;35mY8P                   
\033[0;35m888                \033[0;34m            888 \033[1;35m                       
\033[0;35m888      .d88b.   \033[0;34m8888b.   .d88888 \033[1;35m888 88888b.   .d88b.      
\033[0;35m888     d88""88b  \033[0;34m   "88b d88" 888 \033[1;35m888 888 "88b d88P"88b 
\033[0;35m888     888  888 .\033[0;34md888888 888  888 \033[1;35m888 888  888 888  888 
\033[0;35m888     Y88..88P \033[0;34m888  888 Y88b 888 \033[1;35m888 888  888 Y88b 888 
\033[0;35m88888888 "Y88P"  \033[0;34m"Y888888  "Y88888 \033[1;35m888 888  888  "Y88888 
\033[0;35m                                   \033[1;35m                  888 
\033[0;35m                                   \033[1;35m            Y8b d88P 
\033[0;35m                                   \033[1;35m             "Y88P\033[0m

          \033[1;30m[+] I'm redirecting you to the hub...""")

time.sleep(1)
os.system("cls")

print("""

\033[0;35m888                 \033[0;34m           888 \033[1;35md8b                   
\033[0;35m888                 \033[0;34m           888 \033[1;35mY8P                   
\033[0;35m888                \033[0;34m            888 \033[1;35m                       
\033[0;35m888      .d88b.   \033[0;34m8888b.   .d88888 \033[1;35m888 88888b.   .d88b.      
\033[0;35m888     d88""88b  \033[0;34m   "88b d88" 888 \033[1;35m888 888 "88b d88P"88b 
\033[0;35m888     888  888 .\033[0;34md888888 888  888 \033[1;35m888 888  888 888  888 
\033[0;35m888     Y88..88P \033[0;34m888  888 Y88b 888 \033[1;35m888 888  888 Y88b 888 
\033[0;35m88888888 "Y88P"  \033[0;34m"Y888888  "Y88888 \033[1;35m888 888  888  "Y88888 
\033[0;35m                                   \033[1;35m                  888 
\033[0;35m                                   \033[1;35m            Y8b d88P 
\033[0;35m                                   \033[1;35m             "Y88P\033[0m

          \033[1;30m[-] I'm redirecting you to the hub...""")

time.sleep(1)
os.system("cls")

print("""

\033[0;35m888                 \033[0;34m           888 \033[1;35md8b                   
\033[0;35m888                 \033[0;34m           888 \033[1;35mY8P                   
\033[0;35m888                \033[0;34m            888 \033[1;35m                       
\033[0;35m888      .d88b.   \033[0;34m8888b.   .d88888 \033[1;35m888 88888b.   .d88b.      
\033[0;35m888     d88""88b  \033[0;34m   "88b d88" 888 \033[1;35m888 888 "88b d88P"88b 
\033[0;35m888     888  888 .\033[0;34md888888 888  888 \033[1;35m888 888  888 888  888 
\033[0;35m888     Y88..88P \033[0;34m888  888 Y88b 888 \033[1;35m888 888  888 Y88b 888 
\033[0;35m88888888 "Y88P"  \033[0;34m"Y888888  "Y88888 \033[1;35m888 888  888  "Y88888 
\033[0;35m                                   \033[1;35m                  888 
\033[0;35m                                   \033[1;35m            Y8b d88P 
\033[0;35m                                   \033[1;35m             "Y88P\033[0m

          \033[1;30m[/] I'm redirecting you to the hub...""")

time.sleep(1)
os.system("cls")

print("""

\033[0;35m888                 \033[0;34m           888 \033[1;35md8b                   
\033[0;35m888                 \033[0;34m           888 \033[1;35mY8P                   
\033[0;35m888                \033[0;34m            888 \033[1;35m                       
\033[0;35m888      .d88b.   \033[0;34m8888b.   .d88888 \033[1;35m888 88888b.   .d88b.      
\033[0;35m888     d88""88b  \033[0;34m   "88b d88" 888 \033[1;35m888 888 "88b d88P"88b 
\033[0;35m888     888  888 .\033[0;34md888888 888  888 \033[1;35m888 888  888 888  888 
\033[0;35m888     Y88..88P \033[0;34m888  888 Y88b 888 \033[1;35m888 888  888 Y88b 888 
\033[0;35m88888888 "Y88P"  \033[0;34m"Y888888  "Y88888 \033[1;35m888 888  888  "Y88888 
\033[0;35m                                   \033[1;35m                  888 
\033[0;35m                                   \033[1;35m            Y8b d88P 
\033[0;35m                                   \033[1;35m             "Y88P\033[0m

          \033[1;30m[+] I'm redirecting you to the hub...""")
time.sleep(5)
os.system("cls")

os.system(f"title Numb Tools V2 /// Logged In As: {hn}")


print(f"""                                                
                    \033[1;30m[+]  \033[0;32mWelcome to Hub of Numb Tools [V2.0]                                     


            \033[1;35m          ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ \033[0m
            \033[1;35m          ████╗  ██║██║   ██║████╗ ████║██╔══██╗\033[0m
            \033[1;35m          ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝\033[0m
            \033[1;35m          ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗\033[0m
            \033[1;35m          ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝\033[0m
            \033[1;35m          ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ \033[0m
                                                - Created by \033[1;34m@bbbb_bbbb
                           
                             {Fore.MAGENTA}[{Fore.MAGENTA}{Fore.RESET}1{Fore.RESET}{Fore.MAGENTA}]{Fore.MAGENTA}{Fore.RESET} Webhook Spammer
                             {Fore.MAGENTA}[{Fore.MAGENTA}{Fore.RESET}2{Fore.RESET}{Fore.MAGENTA}]{Fore.MAGENTA}{Fore.RESET} Webhook Deleter
                             {Fore.MAGENTA}[{Fore.MAGENTA}{Fore.RESET}3{Fore.RESET}{Fore.MAGENTA}]{Fore.MAGENTA}{Fore.RESET} Exit\n""")

print(f'{Fore.RESET}|\n└─ {Fore.RESET}{Fore.CYAN}INPUT{Fore.CYAN}{Fore.RESET} → ', end='')

choice = int(input(''))

if choice not in [1, 2, 3, 4]:
    print(f'|\n└─ {Fore.RESET}{Fore.RED}ERROR{Fore.RED}{Fore.RESET} → Invaid Selection Pick the Right Selection')
    wait(1)
    print(f'|\n└─ {Fore.RESET}{Fore.YELLOW}INPUT{Fore.YELLOW}{Fore.RESET} → Press Enter To Exit ', end='')
    input('')
    print(f'|\n└─ {Fore.RESET}{Fore.RED}CLOSING{Fore.RED}{Fore.RESET} → Closing In 5 Seconds...')
    time.sleep(5)
    sys.exit
if choice == 1:
    webhook = str(input(f"|\n└─ {Fore.RESET}{Fore.CYAN}WEBHOOK URL{Fore.CYAN}{Fore.RESET} → "))
    message = str(input(f"|\n└─ {Fore.RESET}{Fore.CYAN}MESSAGE{Fore.CYAN}{Fore.RESET} → "))
    while True:
        _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
        if _data.status_code == 204:
            print(f"|\n└─ {Fore.RESET}{Fore.GREEN}SENT{Fore.GREEN}{Fore.RESET} → Message Sent Successfully")

if choice == 2:
  webhook = str(input(f"|\n└─ {Fore.RESET}{Fore.CYAN}WEBHOOK URL{Fore.CYAN}{Fore.RESET} → "))
  requests.delete(webhook)
  print(f"|\n└─ {Fore.RESET}{Fore.GREEN}DELETED{Fore.GREEN}{Fore.RESET} → Webhook Successfully Deleted")
  time.sleep(1)
  print(f'|\n└─ {Fore.RESET}{Fore.YELLOW}INPUT{Fore.YELLOW}{Fore.RESET} → Press Enter To Exit ', end='')
  input('')
  print(f"|\n└─ {Fore.RESET}{Fore.RED}CLOSING{Fore.RED}{Fore.RESET} → Closing in 5 Seconds...")
  time.sleep(5)
  sys.exit
    
if choice == 3:
  print(f'|\n└─ {Fore.RESET}{Fore.YELLOW}INPUT{Fore.YELLOW}{Fore.RESET} → Press Enter To Exit ', end='')
  input('')
  print(f"|\n└─ {Fore.RESET}{Fore.RED}CLOSING{Fore.RED}{Fore.RESET} → Closing in 5 Seconds...")
  time.sleep(5)
  sys.exit
