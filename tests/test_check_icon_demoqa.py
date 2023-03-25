from pages.demoqa import DemoQa


def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.base_url() #проверка
    assert demo_qa_page.icon.exist() #проверка
