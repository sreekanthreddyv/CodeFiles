import HtmlTestRunner
import unittest
from ch_2_1_test import SearchTest
from ch_2_2_test import HomePageTest

search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

smoke_suite = unittest.TestSuite([home_page_tests, search_tests])

with open("SmokeTestReport.html", 'w') as f_obj:
	# Configure HtmlTestRunner with options
	runner = HtmlTestRunner.HTMLTestRunner(
		stream=f_obj,
		report_title='Test Report',
		descriptions=True,
		open_in_browser=True,
		report_name='Smoke Suite'
	)
	runner.run(smoke_suite)
