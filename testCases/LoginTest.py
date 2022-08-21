import time
import unittest
import HtmlTestRunner
from selenium import webdriver

import sys

sys.path.append("C://Users/mikai/PycharmProjects/PythonUnitTestProject_POMBased_OracleDataBaseConnectivity")
from pageObjects.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    baseURL = "http://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.driver)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title is not matching")

    @classmethod
    def testDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C://Users/mikai/PycharmProjects/PythonUnitTestProject_POMBased_OracleDataBaseConnectivity/reports'))
