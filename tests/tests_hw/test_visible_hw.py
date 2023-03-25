from pages.accordion import Accordion
import time
    def test_visible_accordion (browser)
        accordion_page = Accordion(browser)

        accordion_page.visit()
        assert accordion_page.visible()
        accordion_page.click()
        time.sleep(2)
        assert accordion_page.exist()
