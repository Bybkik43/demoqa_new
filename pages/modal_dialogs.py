from pages.base_page import BasePage
from components.components import WebElement

class DialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)


        self.btns_modal_dialog = WebElement(driver, '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(3) > div')
        self.btn_main_icon = WebElement(driver,  '#app > header > a > img')
        self.btn_small_modal = WebElement(driver, '#showSmallModal > ya-tr-span')
        self.btn_large_modal = WebElement(driver, '#showLargeModal > ya-tr-span')
        self.btn_close_small_modal = WebElement(driver, '#closeSmallModal > ya-tr-span')
        self.btn_close_large_modal = WebElement(driver, '#closeLargeModal > ya-tr-span')