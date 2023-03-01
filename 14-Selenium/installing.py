# Bir web otomasyon kütüphanesidir.
# web siteisni gezip etkileşimde bulunabiliriz.

from selenium import webdriver

driver = webdriver.Edge()


url="https://www.youtube.com"

driver.get(url)