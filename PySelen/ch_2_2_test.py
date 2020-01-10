import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		# Create a new Chrome session """
		chrome_driver_path = r"C:\Users\c_srev\Downloads\geckodriver-v0.26.0-win64\chromedriver.exe"
		cls.driver = webdriver.Chrome(chrome_driver_path)
		cls.driver.implicitly_wait(30)
		# Navigate to the application homepage """
		cls.driver.get("https://www.amazon.in/")

	def test_search_field(self):
		# Check search field exist on home page
		try:
			self.assertTrue(self.is_element_present(By.ID, "twotabsearchtextbox"))
		except NoSuchElementException:
			self.driver.back()
			self.driver.back()
			self.assertTrue(self.is_element_present(By.ID, "twotabsearchtextbox"))

	def test_language_option(self):
		# Check language options dropdown on Home Page
		self.assertTrue(self.is_element_present(By.CLASS_NAME, "icp-nav-language"))

	# def test_check_shopping_cart_empty_message(self):
	# 	# Check content of My Shopping Cart block on Home Page
	# 	shopping_cart_icon = self.driver.find_element_by_id("nav-cart-count")
	# 	shopping_cart_icon.click()
	# 	shopping_cart_status = self.driver.find_element_by_class_name("sc-empty-cart-header").text
	# 	self.assertEqual("Your Shopping Cart is empty.", shopping_cart_status)

	def test_check_cart_enabled(self):
		shopping_cart_icon = self.driver.find_element_by_css_selector("span[id=nav-cart-count]")
		self.assertTrue(shopping_cart_icon.is_enabled())

	def test_link_text_hello(self):
		df = self.driver.find_element_by_link_text("Orders")
		df.click()
		self.assertTrue(2, 2)

	def test_check_shopping_cart_by_css_selector(self):
		# shopping_cart_icon = self.driver.find_element_by_css_selector("span.nav-cart-count")
		shopping_cart_icon = self.driver.find_element_by_css_selector("span[id=nav-cart-count]")
		shopping_cart_icon.click()
		shopping_cart_status = self.driver.find_element_by_css_selector("h1.sc-empty-cart-header").text
		self.assertEqual("Your Shopping Cart is empty.", shopping_cart_status)

	@classmethod
	def tearDownClass(cls) -> None:
		# Close the browser window
		cls.driver.quit()

	def is_element_present(self, how, what):
		"""
		 Utility method to check presence of an element on page
		 :params how: By locator type
		 :params what: locator value
		 """
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException:
			return False
		else:
			return True


if __name__ == '__main__':
	unittest.main(verbosity=2)
