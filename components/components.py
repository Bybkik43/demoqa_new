from selenium.webdriver.common.by import By
class WebElement:
    def __init__(self, driver, loc = " "):
        self.driver = driver
        self.loc = loc
    def click (self):
        self.find_element().click()
    def find_element(self):
        return self.find_element(By.CSS_SELECTOR, self.loc)
    def get_text (self):
        return str(self.find_element().text)

    def visible (self):
        return self.find_element().is_displayed()
    def find_elements(self):
        return self.find_elements(By.CSS_SELECTOR, self.loc)

    def check_count_elements(self, count: int):
        if count == len(self.find_elements()):
            return True
        else:
        return False
    def send_keys (self, text =str()):
        self.find_element()send_keys(text)
