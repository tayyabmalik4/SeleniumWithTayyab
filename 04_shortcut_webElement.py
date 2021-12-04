from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("txtUsername").send_keys("Admin")
pas = driver.find_element_by_id("txtPassword").send_keys("admin123")
loginbtn = driver.find_element_by_class_name("button").click()
driver.quit()