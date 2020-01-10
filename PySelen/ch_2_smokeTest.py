import unittest
from ch_2_2_test import HomePageTest
from ch_2_1_test import SearchTest

# Get all the tests from HomePageTest and SearchTest
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
