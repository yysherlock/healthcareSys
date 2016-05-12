from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
import random

def getUrls(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return []
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        #elems = bsObj.findAll("", {"href" : re.compile("^(http:\/\/.+)")})
        elems = bsObj.findAll("a", {"href" : re.compile(".*")})
        titles = [elem["title"] for elem in elems if "title" in elem.attrs]
        """
        ## Get Names
        names = [elem.get_text() for elem in elems]
        for name in names: print(name)
        """
        urls = [elem["href"] for elem in elems]
        for title in titles: print(title)

    except AttributeError as e:
        return []

    return urls

def getUrls0(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return []
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        urls = [link.attrs["href"] for link in bsObj.findAll("a") if "href" in link.attrs]
    except AttributeError as e:
        return []

    return urls

def getArticleLinks(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return []
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        elems = bsObj.find("div", {"id" : "bodyContent"}).findAll("a", {"href" : re.compile("^(\/wiki\/)((?!:).)*$")}) # tag, attribute-value, keywords
        #print("LENGTH: "+str(len(elems)))
        links = [elem["href"] for elem in elems]
    except AttributeError as e:
        return None

    return links

#urls = getUrls("http://en.wikipedia.org/wiki/Kevin_Bacon")
#urls0 = getUrls0("http://en.wikipedia.org/wiki/Kevin_Bacon")
#print(urls)
#print(len(urls));print(len(urls0))
# for x in urls: print(x)

links = getArticleLinks("http://en.wikipedia.org/wiki/Kevin_Bacon")
for link in links: print(link)
print(len(links))
