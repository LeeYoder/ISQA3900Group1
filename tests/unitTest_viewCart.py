import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "lwyoder"
        pwd = "1Usr5oth"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://isqagroup1.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        driver.get("http://isqagroup1.pythonanywhere.com")
        time.sleep(3)
        # assert "Logged in"
        elem = driver.find_element_by_xpath("/html/body/header/div/ul/li[3]/a").click()

        time.sleep(5)
        try:
            # attempt to find the 'Logout' button - if found, logged in
            elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li[1]/a")

            assert True

        except NoSuchElementException:
            self.fail("Game List does not appear when Games is clicked")
            assert False

    time.sleep(2)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
