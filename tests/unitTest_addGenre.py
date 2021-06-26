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
        name = "test"


        driver = self.driver
        driver.maximize_window()
        driver.get("http://isqagroup1.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://isqagroup1.pythonanywhere.com/admin/BoardGameLand/genre/add/")
        time.sleep(3)
        elem = driver.find_element_by_id("id_name")
        elem.send_keys(name)
        time.sleep(3)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(3)
        try:
            # attempt to find the 'Logout' button - if found, logged in
           elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/h1")

           assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
