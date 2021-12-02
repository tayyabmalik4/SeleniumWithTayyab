from selenium import webdriver

path="C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(path)
# driver.get("https://www.amazon.com/")
driver.get("https://www.xiramsoft.com/")
print(driver.title)
driver.quit()