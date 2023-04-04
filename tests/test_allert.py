
import allure
from pages.allerts import Allerts
import time
@allure.title(' проверка видимости алерта ')
def test_alert(browser):
    alert_page = Allerts(browser)
    alert_page.visit()
    assert not alert_page.alert()

    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert()

@allure.title('подтверждение и текст алерта')
def test_alert_test(browser):
    alert_page = Allerts(browser)
    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert().text('You clicked a button')
    alert_page.alert().accept()
    assert not alert_page.alert()

@allure.title('  отмена алерта ')
def test_confirm(browser):
    alert_page = Allerts(browser)
    alert_page.visit()
    alert_page.btn_confirm.click()
    time.sleep(2)
    alert_page.dismiss()
    assert alert_page.comfirmResult.get_text() ==('You selected Cancel')

@allure.title(' проверка ввода текста алерт ')
def test_pronpt(browser):
    alert_page = Allerts(browser)
    alert_page.visit()
    alert_page.btn_promt.click()
    time.sleep(2)
    alert_page.alert().send_keys('Саша')
    alert_page.alert().accept()
    assert alert_page.promtResult.get_text() == ('You entered Саша')
    time.sleep(2)