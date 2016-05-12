from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src" : re.compile("\.\.\/img\/gifts\/img[0-9]+\.jpg")})

for image in images:
    print("IMAGE: "+str(image))
    print("SRC1: "+image["src"]) # TagElement["attribute"]
    print("SRC2: "+image.attrs["src"]) # TagElement.attrs["attribute"]
