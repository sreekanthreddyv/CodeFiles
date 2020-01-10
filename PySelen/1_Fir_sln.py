from selenium import webdriver

driver = webdriver.Firefox()

driver.implicitly_wait(30)

driver.get("https://www.google.com/")

src = driver.find_element_by_name("q")

src.clear()
src.send_keys("n1tr0g3n")
src.submit()

driver.quit()
