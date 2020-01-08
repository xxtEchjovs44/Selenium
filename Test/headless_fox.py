from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True
#driver = webdriver.Chrome("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Library/chromedriver")
driver = webdriver.Firefox(options=options, executable_path='/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Library/geckodriver')

driver.get("https://onehr.ge.com")

username = driver.find_element_by_id("username")
username.clear()
username.send_keys("502694399")

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("On3H8M0n20191en")

driver.find_element_by_name("submitFrmShared").click()
time.sleep(20)
driver.save_screenshot("screenshot.png")

driver.get(
    "https://onehr.ge.com/psp/prtl/GE_US2_SITE/EMPL/s/WEBLIB_GE_UTIL.GE_FUNCLIB_FLD.FieldFormula"
    ".IScript_BuildNav_JQMega?LType=C&LName=GE_PAY_SUMMARY&PFldr=PORTAL_ROOT_OBJECT")
time.sleep(5)
driver.save_screenshot("screenshot2.png")

if 'Pay History' in driver.page_source:
    print("Article Present")
else:
    print("Article Absent")
