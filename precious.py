from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("D:/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.w3schools.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)