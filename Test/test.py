#import webdriver from selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#load desired browser
driver = webdriver.Chrome("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Library/chromedriver")
System.setProperty("webdriver.gecko.driver", "/Users/username/Downloads/geckodriver");
#set page time out
driver.set_page_load_timeout("10")

driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Manchester United")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
#time.sleep(4)
driver.quit()
