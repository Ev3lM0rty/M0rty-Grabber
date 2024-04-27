import requests
from urllib.parse import urlparse
import os
import sys
import time
import json
import getpass
from socket import gethostbyname
from base64 import b64decode
from platform import system
from random import sample
import re
from multiprocessing.dummy import Pool
from time import time as timer
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore, Style, init
from pprint import pprint

warnings.simplefilter('ignore', InsecureRequestWarning)

init(autoreset=True)

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
gray = '\033[37m'
white = '\033[0m'

current_year = time.strftime("%y")
current_month = time.strftime("%m")

os.system('cls')

def display_menu():
    print('''
    
  __  __  ___       _            _____           _     _               
 |  \/  |/ _ \     | |          / ____|         | |   | |              
 | \  / | | | |_ __| |_ _   _  | |  __ _ __ __ _| |__ | |__   ___ _ __ 
 | |\/| | | | | '__| __| | | | | | |_ | '__/ _` | '_ \| '_ \ / _ \ '__|
 | |  | | |_| | |  | |_| |_| | | |__| | | | (_| | |_) | |_) |  __/ |   
 |_|  |_|\___/|_|   \__|\__, |  \_____|_|  \__,_|_.__/|_.__/ \___|_|   
                         __/ |                                         
                        |___/                                          
\t\tTelegram Channel Link : t.me/Ev3l_m0rty_Channel / Telegram Admin Link: t.me/Ev3l_m0rty
\t\t\ |1| Grabb domains From 'topmillion.net'.
\t\t\ |2| Grabb domains From 'dubdomain.com'. ''')
display_menu()

def get_user_choice():
    choice = input('\t\t\ Enter Your option Number (1-2): ')
    return choice

def fetch_domains_topmillion(first_page, last_page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    for page in range(int(first_page), int(last_page)):
        url = f"https://www.topmillion.net/pages/websites/page/{page}/"
        response = requests.get(url, headers=headers, timeout=15).text  # Changed from .content to .text
        if "All websites" in response:  # Now comparing with a string directly
            domains = re.findall('https://(.*?)?w=400" alt="Thumbnail" />', response)
            for domain in domains:
                clean_domain = domain.replace('?', '')
                print('\t\t[+] Retrieved domain : ' + clean_domain)
                with open("domains.txt", "a") as file:
                    file.write("http://" + clean_domain + "\n")

def fetch_domains_dubdomain(start_page, end_page):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
    for page in range(int(start_page), int(end_page)):
        url = f"https://www.dubdomain.com/index.php?page={page}"
        content = requests.get(url, headers=headers, timeout=15).text
        if 'Recently Analyzed' in content:
            domains = re.findall('data-src="(.*?)"', content)
            for domain in domains:
                clean_domain = domain.replace('https://www.google.com/s2/favicons?domain_url=', '')
                print('\t\t[+] Retrieved domain : ' + clean_domain)
                with open("domains.txt", "a") as file:
                    file.write("http://" + clean_domain + "\n")

def main():
    choice = get_user_choice()
    if choice == '1':
        first_page = input('\t\t[!] Enter The First Page : ')
        last_page = input('\t\t[!] Enter The Last Page : ')
        fetch_domains_topmillion(first_page, last_page)
    elif choice == '2':
        start_page = input('\t\t[!] Enter The First Page : ')
        end_page = input('\t\t[!] Enter The Last Page : ')
        fetch_domains_dubdomain(start_page, end_page)
    else:
        print('\t\t ! False input !')

if __name__ == '__main__':
    main()
