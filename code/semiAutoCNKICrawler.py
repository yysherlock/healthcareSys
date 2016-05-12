# -*- coding = utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen
import requests
import re
import os
import sys
import time
import random

driver = None

cat = u'医药卫生科技'

def generateCNKICookieString(savedCookies, names):
    s = 'AutoIpLogin=;'
    for cookie in savedCookies:
        if cookie['name'] in names:
            if cookie['name'] == 'RsPerPage': cookie['value'] = 50
            s += cookie['name'] + '=' + str(cookie['value']) + ';'
    return s

def Starting(mainpage, url):
    global driver,cat
    driver = webdriver.PhantomJS(executable_path = os.environ['PhantomJS_PATH'])
    driver.get(mainpage)
    driver.implicitly_wait(1) #time.sleep(1)
    #print(driver.get_cookies())
    actions = ActionChains(driver)
    menu = driver.find_element_by_css_selector(".reallclass") #
    actions.move_to_element(menu).perform(); driver.implicitly_wait(2); time.sleep(2)
    hidden_submenu = driver.find_element(By.PARTIAL_LINK_TEXT, cat)
    actions.click(hidden_submenu).perform();
#    cnt = 4
#    while cnt < 10:
#        with open(str(cnt)+'.html','w') as f:
#            driver.implicitly_wait(0.5);
#            time.sleep(0.5)
#            f.write(str(BeautifulSoup(driver.page_source, "html.parser")))
#            cnt += 0.5
    driver.implicitly_wait(2); time.sleep(2); driver.implicitly_wait(2); time.sleep(2);
    #print(str(BeautifulSoup(driver.page_source, "html.parser")))

    cookieString = generateCNKICookieString(driver.get_cookies(),['RsPerPage','ASP.NET_SessionId','SID_grid','LID','c_m_LinID'])
    header = {'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, */*',
    'Cookie' : cookieString
    }
    savedCookies = driver.get_cookies()
#    for cookie in savedCookies:
#        for k,v in cookie.items():
#            print(k,v)
    #bsObj = BeautifulSoup(driver.page_source, "html.parser")
    #print(bsObj)

    #driver.close()
    return header

def getHeader(url):
    cookieString = 'ASP.NET_SessionId=q5hgvh55prruyg55mbhmk345;LID=WEEvREcwSlJHSldTTGJhYlN2Y0NxVStVc2RpUnZRYUJmMEZzaCtSK1dlNk1xTVhRWEhnem80WFJYQmZhM0xIWCtZVT0;SID=91001;SID_kcms=202121;UserDownLoadsKcms=2013%u5E74%u4E2D%u56FDCHINET%u7EC6%u83CC%u8010%u836F%u6027%u76D1%u6D4B%21cjfq%21cjfd2014%21kghl201405001%7C;UserSeesKcms=2011%u5E74%u4E2D%u56FD%u6076%u6027%u80BF%u7624%u53D1%u75C5%u548C%u6B7B%u4EA1%u5206%u6790%21cjfq%21cjfdlast2015%21zhlu201501001%7Cp38MAPK%u4FE1%u53F7%u901A%u8DEF%u4E0E%u80BA%u7EA4%u7EF4%u5316%21%21%21%7C%u4E2D%u836F%u6307%u7EB9%u56FE%u8C31%u6280%u672F%u8FDB%u5C55%u53CA%u672A%u6765%u53D1%u5C55%u65B9%u5411%u5C55%u671B%21cjfq%21cjfdhis2%21zcyo201322003%7C%u4E2D%u56FD%u9AD8%u8840%u538B%u9632%u6CBB%u6307%u53572010%21cjfq%21cjfd2011%21zggz201108003%7C2013%u5E74%u4E2D%u56FDCHINET%u7EC6%u83CC%u8010%u836F%u6027%u76D1%u6D4B%21cjfq%21cjfd2014%21kghl201405001%7C%u7A7A%u5FC3%u62C9%u529B%u9489%u9501%u5B9A%u677F%u4E0E%u7A7A%u5FC3%u9489%u56FA%u5B9A%u80A1%u9AA8%u9888%u9AA8%u6298%u7684%u751F%u7269%u529B%u5B66%u7814%u7A76%21%21%21%7C;c_m_LinID=LinID=WEEvREcwSlJHSldTTGJhYlN2Y0NxVStVc2RpUnZRYUJmMEZzaCtSK1dlNk1xTVhRWEhnem80WFJYQmZhM0xIWCtZVT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=05/12/2016 16:15:04;AutoIpLogin=;'
    #['RsPerPage','ASP.NET_SessionId','SID_grid','LID','c_m_LinID'])
    header = {'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
    'Cookie' : cookieString
    }
    #print(cookieString)

    savedCookies = driver.get_cookies()
    driver.close()
    return header

def pageRequestUrl(pageIndex, QueryID):
    return 'http://epub.cnki.net/kns/brief/brief.aspx?curpage=' + str(pageIndex) + \
    '&RecordsPerPage=50&QueryID=' + QueryID + \
    '&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx#J_ORDER'
    """
    with Year:
        ?curpage=2&RecordsPerPage=50&QueryID=0&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&SortType=%e5%b9%b4&PageName=ASP.brief_default_result_aspx&ctl=bd8e9fa1-9003-42ed-bcc8-40c195c75d55&Param=%e5%b9%b4+%3d+'2016'#J_ORDER
    """

def crawl(startPageIdx, endPageIdx):
    for pageIdx in range(startPageIdx, endPageIdx):
        if pageIdx in [1,4,6,9]: continue
        path = 'pdf/' + str(pageIdx)
        if not os.path.exists(path):
            os.makedirs(path)
        QueryID = str(random.randint(0,10))
        url = pageRequestUrl(pageIdx,QueryID)
        h = Starting("http://www.cnki.net/", url)
        #print('header: '+str(h))
        req = request.Request(url, headers=h)
        r = urlopen(req)
        bsObj = BeautifulSoup(r,"html.parser")
        links = bsObj.findAll("a", {"class" : "fz14"})
        flag = False

        for link in links:
            if 'href' in link.attrs:
                articlelink = 'http://epub.cnki.net' + link.attrs['href']
                if not flag:
                    h1 = getHeader(articlelink)
                    flag = True
                req1 = request.Request(articlelink, headers=h1)
                r1 = urlopen(req1)
                finalpage = BeautifulSoup(r1,"html.parser")
                #print(bsObj)
                #sys.exit(0)
                try:
                    title = finalpage.find(id="chTitle").get_text()
                    title = title.replace('/','')
                    title = title.replace('\\','')
                    pdflink = "http://www.cnki.net/" + finalpage.find("", {"class" : " pdf "}).find("a").attrs['href'].strip()
                except:
                    continue
                try:
                    r2 = urlopen(request.Request(pdflink, headers = h1))
                    time.sleep(3)
                    with open(path+"/"+title+".pdf","wb") as f:
                        f.write(r2.read())
                        f.flush()
                except:
                    continue
                time.sleep(30)


if __name__ == "__main__":
    maxiter = int(sys.argv[1])
    startPageIdx = int(sys.argv[2])
    #maxiter = 10
    #startPageIdx = 41
    iteration = 0

    if not os.path.exists('pdf'):
        os.makedirs('pdf')
    while iteration < maxiter:
        endPageIdx = startPageIdx + 20
        crawl(startPageIdx, endPageIdx)
        startPageIdx = endPageIdx
        iteration += 1

        time.sleep(120)

driver.close()
