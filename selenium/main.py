from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # O el navegador que estés utilizando
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()
