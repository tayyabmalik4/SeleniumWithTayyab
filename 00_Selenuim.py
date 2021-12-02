# first of all install selenium using this command------pip install selenium
# seeing the google version and than install the driver
# secend install to chromedriver from chrome using this link----https://chromedriver.chromium.org/downloads
# if we are working in jupyter than we don't need any chrome driver

from selenium import webdriver

path_of_driver = "chromedriver.exe"
driver = webdriver.Chrome(path_of_driver)
# print("Now Lets go to automation system in IT services")
driver.get("http://www.google.com")
title = driver.title
# assert is a build in function. if the assert option is true than go on next code otherwise error occures
assert "Google" in title
print(title)
print(driver.quit)
driver.quit()