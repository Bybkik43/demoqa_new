from pages.demoqa import DemoQa
from pages.element_page import ElementsPage

def test_check_text_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    assert demo_qa_page.text_footer.get_text()=='© 2013-2020 TOOLSQA.COM | ВСЕ ПРАВА ЗАЩИЩЕНЫ.'
def test_check_text_please(browser):
    demo_qa_page = DemoQa(browser)
    el_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.bth_elements.click()
    assert el_page.text_please.get.text() == 'Please select an item from left to start practice'

def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()


    assert elements_page.test_page_elements.get_text () == "Elements"
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebarbtn_sidebar_first.exist()



