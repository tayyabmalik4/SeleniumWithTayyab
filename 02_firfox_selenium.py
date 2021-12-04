from selenium import webdriver
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://xiramsoft.com/")
print(driver.title)
print(driver.current_url)