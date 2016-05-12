from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

def getCharacterNames(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return []

    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        """
        print("\n====="+bsObj.get_text()+"=====")
        print(bsObj.findAll(class_="red"))

        print(bsObj.findAll("span", {"class":"green"}))
        print(bsObj.findAll("", {"class":"green"}))
        print(bsObj.findAll("div", {"id":"text"}))
        print(bsObj.findAll("", {"id":"text"}))
        """
        nameList = bsObj.findAll("span", {"class" : "green"}) # type of `nameList`: 'bs4.element.ResultSet'
    except AttributeError as e: # if `html` is None
        return []

    try:
        names = [name.get_text() for name in nameList] # type of `name`: 'bs4.element.Tag'
    except AttributeError as e:
        return []

    return names

names = getCharacterNames("http://www.pythonscraping.com/pages/warandpeace.html")
print(names)
