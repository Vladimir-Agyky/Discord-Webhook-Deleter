'''
Made By Nguard
'''

import requests, sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print("Webhook Deleter\n")

webhook = input("Webhook URL: ")
try:
    r = requests.get(webhook, verify=False)
except:
    print("[-] Invalid URL OR Failed To Load URL")
    sys.exit(1)
if(r.status_code==200):
    print("[*] Webhook Online, We Will Now Try To Delete It...")
else:
    print("[-] Webhook Offline")
    sys.exit(1)
    
requests.delete(webhook)

r = requests.get(webhook, verify=False)
if(r.status_code==404):
    print("[+] Webhook Deleted!")
else:
    print("[-] Failed To Delete")
