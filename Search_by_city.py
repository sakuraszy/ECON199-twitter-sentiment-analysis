
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
    base = "https://www.google.com/search?q="
    for mayor in L:
        filter_info(base+'mayor of'+str(mayor),mayor)
        time.sleep(13)
def filter_info(url:str,city:str):
    result = ''
    headers = { # imitate using a FIrefox to access the webpage
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    res= requests.get(url)
    res.raise_for_status()
    a= res.text
    name=re.findall(r"Office: Mayor of.*since \S*",str(a))
    name= name[1][2:].split(">")
    name= name[1]
    year =re.findall(r"<span><span class=\"BNeawe tAd8D AP7Wnd\">Mayor of[^<]*",str(a))[1][-4:]
    write_csv("result.csv",[city,name,year])
    

def save_csv(D):
    a_file = open("result.csv", "w")
    writer = csv.writer(a_file)
    keys =D.keys()
    for key in keys:
        writer. writerow([key, D[key]])
    a_file. close()

def create_csv(p,head:list):
    path = p
    with open(path,"w") as f:
        csv_write= csv.writer(f)
        csv_head=head
        csv_write.writerow(csv_head)
        
def write_csv(p,data:list):
    with open(p,'a+') as f:
        csv_write= csv.writer(f)
        csv_write.writerow(data)
        
    
create_csv('result.csv',["city","name","year"])
##mayor_list = pd.read_csv("cities_1.csv")
##get the list of city name
##implement the code for the city names

cities =["Adak","Akhiok","Akiachak","Akiak","Akutan"]

get_mayor_year(cities)
