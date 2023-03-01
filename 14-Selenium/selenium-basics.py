
from selenium import webdriver
import time


driver=webdriver.Edge()

#driver=webdriver.Chrome()

url ="http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window() #tam ekran yapar
driver.save_screenshot("github.com-homepage.png") #ss aldı

print(driver.title)

time.sleep(2)
driver.close()
