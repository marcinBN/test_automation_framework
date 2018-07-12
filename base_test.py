import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # OR use direct path -> self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


