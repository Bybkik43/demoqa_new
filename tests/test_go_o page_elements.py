from pages.demoqa import DemoQa
from pages.element_page import ElementsPage

    def test_go_test_elements(browser):
    demo_qa_page = DemoQa(browser)
    element_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url() # проверка
    demo_qa_page.bth_elements()
    assert element_page.equal_url() # проверка


def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.footer_element()
    assert demo_qa_page.base_url()
    assert demo_qa_page.footer_element()


get_text
if srting = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.' in demo_qa_page.footer_element():
    print("ok")
else:
    print("false")

