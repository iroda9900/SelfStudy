from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

URL1 = driver.get("https://letskodeit.teachable.com/p/practice")
print(driver.title)


URL2 = driver.get("https://www.target.com/")
print(driver.title)
time.sleep(5)
driver.back()
print("Its URL1 : " ,driver.title)
time.sleep(5)
driver.forward()
print("Its URL2 : ", driver.title)

driver.close()
print("Test passed")