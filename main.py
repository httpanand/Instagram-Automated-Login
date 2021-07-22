from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.instagram.com")
time.sleep(3)

element = driver.find_element_by_xpath("//input[@name='username']")
username = input("Enter Username")
element.send_keys(username)

element = driver.find_element_by_xpath("//input[@name='password']")
password = input("Enter Password")
element.send_keys(password)

element.send_keys(Keys.RETURN)
