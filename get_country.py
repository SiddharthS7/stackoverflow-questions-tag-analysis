import requests
from bs4 import BeautifulSoup
import pandas as pd

def country(userid):
    url="https://stackoverflow.com"+userid

    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')

    first=soup.find_all(class_="wmx2 truncate")
    parent=first[0].parent
    wmx2=parent.find("div")

    final=wmx2.string.strip()

    return str(final)

def userid(qid):
    url="https://stackoverflow.com/questions/"+qid

    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')

    first=soup.find_all(class_="user-action-time")
    for i in first:
        if 'asked' in i.get_text():
            user=i.find_next_sibling().find("a").get("href")

    try:
        print(country(user))

    except IndexError:
        print("No country provided")

df=pd.read_csv("dataset.csv")
qid=(df["Id"])

for j in qid:
    userid(str(j))