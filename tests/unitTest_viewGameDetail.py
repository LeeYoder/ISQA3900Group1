import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()

        driver.get("http://isqagroup1.pythonanywhere.com")
        time.sleep(3)
        # assert "Logged in"
        elem = driver.find_element_by_xpath("/html/body/header/div/ul/li[2]/a").click()
        elem = driver.find_element_by_xpath("/html/body/ul[2]/li[1]/a").click()

        time.sleep(5)
        try:
            # attempt to find the 'Logout' button - if found, logged in
            elem = driver.find_element_by_xpath("/html/body/ul/li[4]")

            assert True

        except NoSuchElementException:
            self.fail("Game List does not appear when Games is clicked")
            assert False

    time.sleep(2)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
