from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# ---THIS IS old version and now it is not used
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# pas = driver.find_element_by_id("txtPassword").send_keys("admin123")
# loginbtn = driver.find_element_by_class_name("button").click()

# ----this is professionally method to use By class to find elements in the browser
# driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
# pas = driver.find_element(By.ID,"txtPassword").send_keys("admin123")
# loginbtn = driver.find_element(By.CLASS_NAME,"button").click()

# ----if we want to don't use the By class than we simply use values of name and id and soo onn
driver.find_element("name","txtUsername").send_keys("Admin")
pas = driver.find_element("id","txtPassword").send_keys("admin123")
loginbtn = driver.find_element("class name","button").click()

driver.quit()