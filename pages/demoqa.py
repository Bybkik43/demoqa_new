
from pages.base_page import BasePage
from components to components WebElement

class DemoQa(BasePage):
    def __init__(self):
        self.base_url = 'https://demoqa.com'
        super().__init__(driver, self.base_url)



    def __int__(self):

        self.icon = WebElement(driver, '#app > header > a' )
        self.bth_elements = WebElement(driver, '#app > div > div >div.home-body > div > div:nth-child(1)')
        self.text_footer = WebElement(driver, ' # app > footer > span')

