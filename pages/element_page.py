from pages.base_page import BasePage
class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)



    self.text.please = WebElement(driver,'# app > div > div > div.row > div.col-12.mt-4.col-md-6')
    self.text.elements = WebElement(driver, 'div.playground-header >div')
    self.icon.elements = WebElement(driver,
    self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
    self.btn_sidebar_first_text = WebElement(driver,''
    self.btn_sidebar_first_check_box = WebElement(driver,'')