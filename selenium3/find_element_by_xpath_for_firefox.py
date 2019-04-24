running environment: ipython

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://qa3912.lab.fp.f5net.com/f5-w-68747470733a2f2f31302e3139322e3133372e3431$$/owa/#path=/mail")

driver.find_element_by_xpath("//input[@name='username']").send_keys("silk1")

driver.find_element_by_xpath("//input[@name='password']").send_keys("password1!a")

driver.find_element_by_xpath("//input[@value='Logon']").click()

obj = driver.find_element_by_xpath("//span[text()='Test new subject 2019-04-23T17:48:47.315000']")
