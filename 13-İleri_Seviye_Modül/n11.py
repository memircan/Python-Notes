from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup

url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html=requests.get(url).content
soup= BeautifulSoup(html,"html.parser")


list=soup.find_all("li",{"class":"column"},limit=1)

for li in list:
    #name=li.div.a.h3.text.strip()
    link=li.div.a.get("href")

    print(link)
    




