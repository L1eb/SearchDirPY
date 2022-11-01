import requests
import os
import cloudscraper
import httplib2
import http
from http import HTTPStatus
import time


scraper = cloudscraper.create_scraper()
url = input("Past url :  ")
r = requests.get(url)
r = scraper.get(url)
print(r.url)
yes = input("is this url right ? Y/N :  ")
if yes == 'Y':
    True
elif yes == 'y':
    True
elif yes == 'n':
    False
elif yes == 'N':
    False
os.system('cls')
print(""" 

        [#]smalldirlist.txt

        [#]dirlist.txt                [#]smalldirlist2.txt

        [#]mediumdirlist.txt          [#]mediumdirlist2.txt

        [#]bigdirlist.txt             [#]bigdirlist2.txt


            """)
filee = input("select a dirlist file :  ")

f = open(filee, "r")
result = f.readline()

scraper = cloudscraper.create_scraper()

with open(filee, errors='ignore') as temp_f:
    while result:
        result = f.readline()
        line = result.strip()
        u = url+'/'+line
        d = requests.get(u)
        scraper = cloudscraper.create_scraper()
        if d.status_code == 404:
            False

        elif d.status_code == 200:
            time.sleep(1)
            print("\n[#] dir found !", u )

    
            


f.close()
