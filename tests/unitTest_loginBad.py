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
        pwd = "badpass"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://isqagroup1.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://isqagroup1.pythonanywhere.com")
        time.sleep(3)
        #assert "did not Login"
        try:
            # attempt to find the 'Logout' button - if found, logged in
           elem = driver.find_element_by_xpath("/html/body/header/div/ul/li[4]/a")
           self.fail("Login Successful - unwanted")

           assert False

        except NoSuchElementException:
            assert True

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
