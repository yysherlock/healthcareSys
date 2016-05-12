# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    try:
        html = urlopen("http://en.wikipedia.org"+pageUrl)
    except HTTPError as e:
        return
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.h1.get_text(); print(title)
        firstPara = bsObj.find("div",class_="mw-body-content").find("p"); print(firstPara)
        editLink = bsObj.find("li", {"id" : "ca-edit"}).find("span").find("a").attrs["href"]; print(editLink)
    except AttributeError as e:
        print("页面缺少一些属性！")

    for page in bsObj.findAll("a", {"href" : re.compile("^(\/wiki\/)")}):
        if "href" in page.attrs and page.attrs["href"] not in pages:
            newLink = page.attrs["href"]
            pages.add(newLink)
            print("--------\n"+newLink)
            getLinks(newLink)

getLinks("")
