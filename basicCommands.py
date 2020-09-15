from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://letskodeit.teachable.com/p/practice")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//a[@id='opentab']").click()
time.sleep(5)
#driver.close()
driver.quit()
