import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "lwyoder"
        pwd = "1Usr5oth"
        title = "test"
        description = "test description"
        price = 100


        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin/BoardGameLand/game/add/")
        time.sleep(3)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys(title)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys(description)
        elem = driver.find_element_by_id("id_price")
        elem.send_keys(price)
        elem = Select(driver.find_element_by_id("id_genre"))
        elem.select_by_index(0)
        time.sleep(3)
        elem = driver.find_element_by_name("_save")
        elem.click()
        time.sleep(3)
        try:
            # attempt to find the 'Logout' button - if found, logged in
           elem = driver.find_element_by_xpath("/html/body/")

           assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
