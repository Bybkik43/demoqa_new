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
