import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
url = "http://phoenix.testautomationacademy.in/sign-in"
driver.get(url)
# username
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "username").send_keys("iamfd")
# password
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "password").send_keys("password")
# SignButton
driver.find_element(By.XPATH, "//span[contains(text(), ' Sign in ')]/../..").click()
time.sleep(2)

driver.find_element(By.XPATH, "(//button)[2]").click()
time.sleep(2)
print(driver.find_element(By.XPATH, "//span[contains(text(),'iamfd')]").text)

# driver.find_element(By.XPATH, "//input[@placeholder='Search for a Job or IMEI']").send_keys("JOB_28957")
# driver.find_element(By.XPATH, "//input[@placeholder='Search for a Job or IMEI']").send_keys(Keys.ENTER)
# time.sleep(3)
# driver.find_element(By.XPATH, "//button[contains(text(),'JOB_')]").click()
# time.sleep(3)
