from pages.text_box import Text_boxPage
import allure

@allure.feature('check attr')
@allure.story('Проверка placeholder')
@allure.severity(allure.severity_level.BLOCKER)
def test_placeholder(browser):
    text_box = Text_boxPage(browser)
    text_box.visit()
    assert text_box.full_name.get_dom_attribute('placeholder') == 'Full name'

@allure.feature('check attr')
@allure.story('Проверка упавшего теста')
@allure.severity(allure.severity_level.BLOCKER)
def test_fail():
    assert 111 == 222