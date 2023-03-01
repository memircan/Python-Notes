from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver=webdriver.Edge()
#driver=webdriver.Chrome()


url ="http://github.com"
driver.get(url)

driver.maximize_window()
searchInput = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
time.sleep(1)

searchInput.send_keys("python")
time.sleep(2)

searchInput.send_keys(Keys.ENTER)
time.sleep(2)

#result= driver.page_source
#print(result)

result= driver.find_elements(By.XPATH,'//*[@id="js-pjax-container"]/div/div[3]/div/ul/li[1]/div[2]/div[1]/div[1]/a')

for element in result:
    print(element.text)



driver.close()