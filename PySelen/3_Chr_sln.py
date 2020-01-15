from selenium import webdriver
from time import sleep


chrome_driver_path = r"E:\Python\myTemp\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.google.com")

src = driver.find_element_by_name("q")
src.clear()
src.send_keys("n1tr0g3n")
src.submit()

sleep(3)

driver.quit()

