from pages.accordion import Accordion
import time
def test_visible_accordion(browser)
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.visible()
    accordion_page.section1.click()
    time.sleep(2)
    assert accordion_page.section1.exist()

def test_visible_accordion_default (browser)
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.section2_p_1.visible()
    assert not accordion_page.section2_p_2.visible()
    assert not accordion_page.section3.visible()
