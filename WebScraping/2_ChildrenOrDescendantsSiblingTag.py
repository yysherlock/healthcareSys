from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")

"""
### Children Tag ###
for child in bsObj.find("table", {"id" : "giftList"}).children:
    print(child)

### Descendants Tag ###
for child in bsObj.find("table", {"id" : "giftList"}).descendants:
    print(child)
"""

### Sibling Tag ###
for sibling in bsObj.find("table", {"id" : "giftList"}).tr.next_siblings:
    print(sibling)
"""
print("------")
sibs = bsObj.find("table", {"id" : "giftList"}).tr
print(len(sibs)) # length is 4, and sibs.next_siblings generate its 3 siblings
"""

# .next_siblings and .previous_siblings return a generator
