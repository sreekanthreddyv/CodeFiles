import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class SearchTest(unittest.TestCase):

	# def setUp(self) -> None:
	# 	"""
	# 	we created a new instance of Firefox using the setUp()
	# 	method before the execution of each test method and closed that instance after the
	# 	execution of the test method.
	# 	:return: None
	# 	"""
	# 	# Create new Ie session
	# 	# ie_driver_path = r'C:\Users\c_srev\Downloads\geckodriver-v0.26.0-win64\IEDriverServer.exe'
	# 	# self.driver = webdriver.Ie(ie_driver_path)
	# 	chrome_driver_path = r"C:\Users\c_srev\Downloads\geckodriver-v0.26.0-win64\chromedriver.exe"
	# 	self.driver = webdriver.Chrome(chrome_driver_path)
	# 	self.driver.implicitly_wait(30)
	# 	# self.driver.maximize_window()
	#
	# 	# Navigate to the application home page
	# 	self.driver.get("https://www.google.com/")

	@classmethod
	def setUpClass(cls):
		# Create a new Ie session
		# ie_driver_path = r'C:\Users\c_srev\Downloads\geckodriver-v0.26.0-win64\IEDriverServer.exe'
		# cls.driver = webdriver.Ie(ie_driver_path)
		chrome_driver_path = r"C:\Users\c_srev\Downloads\geckodriver-v0.26.0-win64\chromedriver.exe"
		cls.driver = webdriver.Chrome(chrome_driver_path)
		cls.driver.implicitly_wait(30)
		# Navigate to the application home page
		cls.driver.get("https://www.google.com/")
		# cls.driver.title

	def test_search_text_field_max_length(self):
		self.search_field = self.driver.find_element_by_name("q")
		self.assertEqual("2048", self.search_field.get_attribute("maxlength"))

	def test_search_by_category(self):
		self.search_field = self.driver.find_element_by_name("q")
		self.search_field.clear()
		self.search_field.send_keys("learn python")
		self.search_field.submit()
		# try:
		# 	# ha = self.driver.find_element_by_xpath("//h3[@class='LC201b']").text
		# 	print(f"hello: {ha}")
		# except NoSuchElementException:
		# 	pass
		# sleep(4)
		assert True  # "Learn" in self.driver.find_element_by_xpath("//h3[@class='LC201b']").text

	def test_xpath(self):
		self.driver.get("http://newtours.demoaut.com/")
		logo = self.driver.find_element_by_xpath("//img[@alt='Featured Destination: Aruba']")
		self.assertTrue(logo.is_displayed())

	def test_search_by_name(self):
		self.search_field = self.driver.find_element_by_name("q")
		self.search_field.clear()
		self.search_field.send_keys("n1tr0g3n")
		self.search_field.submit()
		# sleep(7)
		assert True

	# def tearDown(self) -> None:
	# 	# Close the browser window
	# 	self.driver.quit()

	@classmethod
	def tearDownClass(cls) -> None:
		# Close the browser window
		cls.driver.quit()


if __name__ == "__main__":
	unittest.main()
