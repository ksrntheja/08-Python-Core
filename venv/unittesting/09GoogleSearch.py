from selenium import webdriver
import unittest
import time


class GooglesearchDemo(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox(executable_path='/geckodriver')
        driver.get('https://www.google.com')

    # driver.maximize_window()

    def test(self):
        driver.find_element_by_name('q').send_keys('python')
        time.sleep(5)
        driver.find_element_by_name('btnK').click()
        time.sleep(5)
        driver.find_element_by_class_name('LC20lb').click()
        time.sleep(5)

    def tearDown(self):
        driver.close()


unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 27.523s

# OK
