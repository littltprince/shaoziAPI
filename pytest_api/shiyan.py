from selenium import webdriver
import time
a=webdriver.Chrome()
a.get("http://www.baidu.com")
a.maximize_window()
a.find_element_by_id('kw').send_keys('哈哈哈 kimoji')
a.find_element_by_xpath("")
#相对定位  以//开头    //标签名[@属性名=值 and 或者or ]例如  //input[@name="wd" and @autocomplete="off"]
#层级定位 //父标签[@属性名-值]/子标签[@属性名-值]//子孙标签[@属性名-值] 
#绝对定位 依赖页面的顺序和位置 以/开头，例如/html/div/...

a.find_element_by_id('su').submit()
time.sleep(15)

