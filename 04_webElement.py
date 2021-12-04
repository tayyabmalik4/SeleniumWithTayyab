from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
# print(type(driver))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# the username is find element by the help of name
username = driver.find_element_by_name("txtUsername")
# print(type(username))
# ---achully there are 3 method which we check---enabled, displayed and selected 
# ---it returns the just true or false
enable_check = username.is_enabled()
print(enable_check)

display_check = username.is_displayed()
print(display_check)

# selected method check the checkbox--- the checkbox is selected or not
# selected= username.is_selected()

# ----before sending the send_key we clear the default value--- it is a good practice
username.clear()

# ----get_attribute is to get the attribute of the value
att = username.get_attribute("type")
print(att)

# ----we also get the css property which we want
cs = username.value_of_css_property("font-family") 
print(cs)

username.send_keys("Admin")

# the password is find by the help of id
pas = driver.find_element_by_id("txtPassword")
enable_check1 = pas.is_enabled()
print(enable_check1)
display_check1 = pas.is_displayed()
print(display_check1)
pas.clear()
pas.send_keys("admin123")

# login button is find element by the help of class name
loginbtn = driver.find_element_by_class_name("button")
loginbtn.click()

driver.quit()