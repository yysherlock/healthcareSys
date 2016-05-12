from selenium import webdriver
import time
import os

driver = webdriver.PhantomJS(executable_path = os.environ['PhantomJS_PATH'])
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()
