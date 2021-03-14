from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(25) # seconds
driver.get("http://habr.com/ru/post/250921/")
#myDynamicElement = driver.find_element_by_id("myDynamicElement")
myDynamicElement = driver.find_element_by_id("Python")
