from pages.demoqa import DemoQa
from pages.element_page import ElementsPage
def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.bth_elements.click()
    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    elements_page.equal_url()
    assert elements_page.equal_url()