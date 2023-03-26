from pages.base_page import BasePage
from components to components WebElement
class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)


        self.section1 = WebElement(driver, '#section1Content > p')
        self.section2_p_1 = WebElement(driver, '#section2Content > p: nth-child(1)')
        self.section2_p_2 = WabElement(driver, '#section2Content > p: nth-child(2)')
        self.section3 = WebElement(driver, '#section3Content > p')