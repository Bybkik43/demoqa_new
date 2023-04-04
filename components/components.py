import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

class WebElement:
    def __init__(self, driver, locator = " ", locator_type = 'css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type
    def click (self):
        self.find_element().click()
    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)
    def get_text (self):
        return str(self.find_element().text)

    def visible (self):
        return self.find_element().is_displayed()
    def find_elements(self):
        return self.find_elements(self.get_by_type(), self.locator)

    def check_count_elements(self, count: int):
        if count == len(self.find_elements()):
            return True
        else:
            return False
    def send_keys (self, text =str()):
        self.find_element().send_keys(text)
    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())
    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)
    def get_dom_attribute(self, name: str):
        value = self.find_elements().get_dom_attribute(name)
        if value is None:
            return False
        if len(value) > 0:
            return True
    def get_by_type(self):
        if self.locator_type =='id':
            return By_ID
        elif self.locator_type =='name':
            return By_name
        elif self.locator_type =='xpath':
            return By_XPATH
        elif self.locator_type =='css':
            return By_CSS
        elif self.locator_type =='class':
            return By_CLASS_NAME
        elif self.locator_type =='link':
            return By_LINK_TEXT
        else:
            print("Locator type" + self.locator_type + "not correct")

    def scroll_to_element(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight):", self.find_element())
    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False



