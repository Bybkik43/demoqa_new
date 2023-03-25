from pages.elements_page import ElementsPage
import time

    def test_visible_bth_sidebar(browser):
        elements_page = ElementsPage(browser)
        elements_page.visit()
        #elements_page_btn_sidebar_first.click()
        #time.sleep(3)
        #assert elements_page_btn_sidebar_first.textbox.exist()
        assert elements_page_btn_sidebar_first.textbox.visible()
        assert not elements_page_btn_sidebar_first.textbox.visible()
    def test_not_visible_bth_sidebar(browser):
        elements_page = ElementsPage (browser)
        elements_page.visit()
