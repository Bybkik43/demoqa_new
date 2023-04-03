from pages.base_page import BasePage
from components.components import WebElement


class Text_boxPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text_box'
        super().__init__(driver, self.base_url)

        self.text_box.name = WebElement(driver,)
        self.placeholder = WebElement(driver, //*[@id="userName-label"])