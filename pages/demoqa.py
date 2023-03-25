
from selenium.common.expections import NoSuchElementException

from pages.base_page import BasePage
from components to components WebElement

class DemoQa(BasePage):
    def __init__(self):
        self.base_url = 'https://demoqa.com'
        super().__init__(driver, self.base_url)

    def exist_icon(self):
        try:
            self.icon.find.element()
        except NoSuchElementException:
            return False
        return True

    def __int__(self):

        self.icon = WebElement(driver, '#app > header > a' )
        self.bth_elements = WebElement(driver, '#app > div > div >div.home-body > div > div:nth-child(1)')
        self.footer_element = WebElement(driver, ' # app > footer > span')

