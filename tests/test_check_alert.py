from pages.allerts import Allerts
import time

def test_check_alert(browser):
    alert_page = Allerts(browser)
    alert_page.visit()
    alert_page.btn_alert.exist()
    alert_page.btn_alert.click()
    time.sleep(5)
    assert alert_page.alert()
