from pages.base_page import BasePage
from components.components import WebElement

class alert(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_alert = WebElement(driver, '#alerButton')
        self.btn_confirm = WebElement(driver, '#confirmButton')
        self.btn_promt = WebElement(driver, '#promtButton')
        self.btn_timer_alert = WebElement(driver, '#timerAlertButton')


