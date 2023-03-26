from pages.demoqa import DemoQa
from pages.element_page import ElementsPage

 def test_go_test_elements(browser):
    demo_qa_page = DemoQa(browser)
    element_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url() # проверка
    demo_qa_page.bth_elements.click()
    assert element_page.equal_url() # проверка






