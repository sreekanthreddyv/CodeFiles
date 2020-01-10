from selenium import webdriver
from time import sleep

ie_driver_path = r'C:\Users\c_srev\Downloads\geckodriver-v0.26.0-win64\IEDriverServer.exe'

driver = webdriver.Ie(ie_driver_path)
driver.implicitly_wait(30)
driver.get("https://www.google.com/")

src = driver.find_element_by_name("q")

src.clear()
src.send_keys("n1tr0g3n")
src.submit()

sleep(3)
driver.quit()