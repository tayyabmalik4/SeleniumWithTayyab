from selenium import webdriver
from selenium.webdriver.chrome import service
# the server pakage is import to avoid the warning to deprecated
from selenium.webdriver.chrome.service import Service

s=Service("chromedriver.exe")

# path="C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.amazon.com/")
# driver.get("https://www.xiramsoft.com/")
print(driver.title)
# driver.quit()