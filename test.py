
import requests
import webbrowser
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.request import urlopen
import re
import pandas as pd
import webbrowser
import sys
import bs4
import time
import csv

def get_mayor_year(L):
    result = {}
    base = "https://www.google.com/search?ei=GJ-mXrDcOYmWsgXr0rGwBw&q="
    for mayor in L:
        try:
            print(mayor)
            result[mayor] = filter_year(base+str(mayor))
        except:
            save_csv(result)
        time.sleep(13)
    return result
def filter_year(url:str):
    result = ''
    headers = { # imitate using a FIrefox to access the webpage
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    res= requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"html.parser")
    a= soup.get_text()
    b=re.findall(r"Office: Mayor of.*since \S*",str(a))
    if len(b)< 1:
        return ""
    for i in b[0]:
        if len(result)==4:
            return result
        try:
            int(i)
            result += i
        except:
            pass
    return result

def save_csv(D):
    a_file = open("result.csv", "w")
    writer = csv.writer(a_file)
    keys =D.keys()
    for key in keys:
        writer. writerow([key, D[key]])
    a_file. close()
    
mayor_list = pd.read_csv("mayor_results.csv")


Mayor_years= get_mayor_year(list(mayor_list["name"]))
save_csv(Mayor_years)
