from selenium import webdriver
import unittest
from time import sleep


class RegisterUser(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		chrome_driver_path = r"C:\Users\c_srev\Downloads\geckodriver-v0.26.0-win64\chromedriver.exe"
		cls.driver = webdriver.Chrome(chrome_driver_path)
		cls.driver.implicitly_wait(30)
		cls.driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

	def test_test_field(self):
		field = self.driver.find_element_by_class_name("form-control")
		field.clear()
		field.send_keys("Hello Hacker")
		btn = self.driver.find_element_by_css_selector("button.btn")
		sleep(2)
		btn.click()
		sleep(2)
		
	def test_sum_field(self):
		sum1 = self.driver.find_element_by_id("sum1")
		sum1.clear()
		sum1.send_keys(2)
		sum2 = self.driver.find_element_by_id("sum2")
		sum2.clear()
		sum2.send_keys(5)
		sleep(0.2)
		btn = self.driver.find_element_by_xpath("//*[contains(text(), 'Get Total')]")
		btn.click()
		sleep(4)

	# def test_button(self):
	# 	btn = self.driver.find_element_by_css_selector("button.btn")
	# 	btn.click()
	# 	sleep(5)

	@classmethod
	def tearDownClass(cls) -> None:
		cls.driver.quit()
