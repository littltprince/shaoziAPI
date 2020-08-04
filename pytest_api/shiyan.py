from selenium import webdriver
import time
a=webdriver.Chrome()
a.get("http://www.baidu.com")
a.find_element_by_id('kw').send_keys('哈哈哈 kimoji')
a.find_element_by_id('su').submit()
time.sleep(15)

