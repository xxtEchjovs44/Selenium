from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Library/chromedriver")
# driver.set_page_load_timeout("10")
driver.get("https://onehr.ge.com")
driver.save_screenshot("ssopage.png")

if 'username' in driver.page_source:
    print('Log in page loading : YES')

    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys("502694399")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("On3H8M0n20191en")

    driver.find_element_by_name("submitFrmShared").click()
    time.sleep(20)

    driver.save_screenshot("page1.png")
    driver.get("https://benefits.ge.com/psp/prtl/GE_US2_SITE/EMPL/h/?tab=DEFAULT")
    if 'Pay Summery' in driver.page_source:
        print('Pay Summery Loading : YES')
        if 'HELP' in driver.page_source:
            print ('Help Loading : YES')
        else:
            print('Help Loading : No')
    else:
        print('Pay Summery Loading : No')

else:
    print('Log in page loading : NO')
