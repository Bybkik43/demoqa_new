from pages.base_page import BasePage
from components.components import WebElement

class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/forms'
        super().__init__(driver, self.base_url)


        self.first_name = WebElement(driver,'#firstName')
        self.last_name = WebElement(driver,'#lastName')
        self.gender = WebElement(driver,'#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2) > label')

