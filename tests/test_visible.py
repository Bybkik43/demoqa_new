from pages.elements_page import ElementsPage
import time
def test_visible_bth_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()

    assert elements_page.btn_sidebar_first.textbox.visible()
    assert not elements_page.btn_sidebar_first.textbox.visible()

    assert elements_page.btn_sidebar_first.checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first.checkbox.visible()

def test_not_visible_bth_sidebar(browser):
    elements_page = ElementsPage (browser)
    elements_page.visit()
