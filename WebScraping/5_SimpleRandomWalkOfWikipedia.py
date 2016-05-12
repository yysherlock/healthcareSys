from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    try:
        html = urlopen("http://en.wikipedia.org"+articleUrl)
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

links = getLinks("/wiki/Kevin_Bacon")
while len(links)>0:
    newArticle = links[random.randint(0,len(links)-1)]
    print(newArticle)
    getLinks(newArticle)
