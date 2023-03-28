from pages.base_page import BasePage
from components.components import WebElement

class DialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)


        self.btns_modal_dialog = WebElement(driver, '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(3) > div')
        self.btn.main_icon = WebElement(driver,  '#app > header > a > img')