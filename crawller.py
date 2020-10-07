import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint

# xml
import xml.etree.ElementTree as ET

headers = {"Accept-Language": "en-US, en;q=0.5"}
base_url = "http://nostalgiamusic.info/"
file = open("urls_full.txt", "a")

tree = ET.parse("./sitemap.xml")
root = tree.getroot()
for child in root:
    print ("Processing " + child[0].text)

    page = requests.get(child[0].text, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')

    listen_div = soup.find_all('a', class_='listen')
    for div in listen_div:
        print(div['href'])
        file.write(base_url + div['href'] + "\n")
        
    sleep(randint(2,10))

file.close()
