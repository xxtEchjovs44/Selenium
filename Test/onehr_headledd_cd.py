from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
driver = webdriver.Chrome("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Library/chromedriver", options=options)
# driver.set_page_load_timeout("10")
driver.get("https://onehr.ge.com")
driver.save_screenshot("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Screenshots/ssopage.png")

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

    driver.save_screenshot("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Screenshots/page1.png")

    content = driver.page_source
    if content.find("Pay Summary"):
        print("Pay Summary Loading : YES")
        if content.find("Filter"):
            time.sleep(2)
            print("Filter text verification : Found")
            if content.find("HELP"):
                time.sleep(2)
                print("HELP text verification : Found")
                if content.find("Retirement Savings Plan (RSP)"):
                    time.sleep(2)
                    print("Retirement Savings Plan Widget : Found")
                    if content.find("Executive Compensation"):
                        time.sleep(2)
                        print("Executive Compensation Widget : Found")
                        if content.find("Health Care"):
                            time.sleep(2)
                            print("Health Care Widget : Found")
                            if content.find("As of:"):
                                time.sleep(2)
                                print("Travel Widget : Found")
                                if content.find("Recognition"):
                                    time.sleep(2)
                                    print("Recognition Widget : Found ")

                                    driver.get(
                                        "https://onehr.ge.com/psp/prtl/GE_US2_SITE/EMPL/s/WEBLIB_GE_UTIL"
                                        ".GE_FUNCLIB_FLD.FieldFormula.IScript_BuildNav_JQMega?LType=C&LName"
                                        "=GE_PAY_SUMMARY&PFldr=PORTAL_ROOT_OBJECT")
                                    time.sleep(5)
                                    driver.save_screenshot("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Screenshots/payhistory.png")
                                    content = driver.page_source
                                    if content.find("Pay History"):
                                        print("Pay History : Successful")
                                        driver.get(
                                            "https://onehr.ge.com/psp/prtl/GE_US2_SITE/EMPL/s/WEBLIB_GE_UTIL"
                                            ".GE_FUNCLIB_FLD.FieldFormula.IScript_BuildNav_JQMega?nodeId=126&LType=C"
                                            "&LName=GE_EDUCATIONAL_LOAN_PROGRAM&PFldr=GE_ADDITIONAL_BENEFITS")
                                        time.sleep(5)
                                        driver.save_screenshot("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Screenshots/education.png")
                                        content = driver.page_source
                                        if content.find("GE Educational Loan Program"):
                                            print("MSG: GE Educational Loan Program Page Loaded Successfully ")
                                            driver.get(
                                                "https://onehr.ge.com/psp/prtl/GE_US2_SITE/EMPL/s/WEBLIB_GE_UTIL"
                                                ".GE_FUNCLIB_FLD.FieldFormula.IScript_BuildNav_JQMega?LType=C&LName=GE_HEALTH_PLAN_SUMMARY&PFldr=GE_HEALTH_CARE")
                                            time.sleep(5)
                                            driver.save_screenshot("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Screenshots/healthplan.png")
                                            content = driver.page_source
                                            if content.find("Benefits Summary"):
                                                print("Health Care Enrollment Summery Page Loaded Successfully!")
                                                driver.get("https://onehr.ge.com/psp/prtl/GE_US2_SITE/EMPL/?cmd=logout")
                                                time.sleep(5)
                                                driver.save_screenshot("/Users/soumyabratadutta/PycharmProjects/Silenium_Test/Screenshots/logout.png")
                                                content = driver.page_source
                                                if content.find(
                                                        "You have been logged out of this application. To completely "
                                                        "log out of Single Sign On, please close your browser."):
                                                    print("Logout Successful")
                                                else:
                                                    print("Logout Not Successful")
                                            else:
                                                print("Health Care Enrollment Summery Page was not able to load!")
                                        else:
                                            print("Wasn't able to load GE Educational Loan Program Page ")
                                    else:
                                        print("Pay History : Failure")
                                else:
                                    print("Could Not Found Recognition Widget")
                            else:
                                print("Travel Widget Unable to Load")
                        else:
                            print("Health Care Widget Unable to Load")
                    else:
                        print("Execution Compensation Widget failed to Load")
                else:
                    print("Retirement Widget failed to load")
            else:
                print("Help Text Verification Not Found")
        else:
            print("Filter Text Verification Not Found")
    else:
        print("Unable to Load Pay Summery!")
else:
    print('Log in page loading : NO')
