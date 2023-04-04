from pages.modal_dialogs import DialogsPage
from pages.demoqa import DemoQa

def test_modal_elements(browser):
    modal_dialogs_page = DialogsPage(browser)
    modal_dialogs_page.visit()
    modal_dialogs_page.btns_modal_dialog.check_count_elements()
    assert modal_dialogs_page.btns_modal_dialog.check_count_elements(5) #(count=5)

def test_navigation_modal_(browser):
    modal_dialogs_page = DialogsPage(browser)
    demo_qa_page = DemoQa(browser)
    modal_dialogs_page.visit()
    modal_dialogs_page.refresh()
    modal_dialogs_page_icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert browser.title == demo_qa_page.pageData['title']
    assert demo_qa_page.equal_url()
    browser.set_window_size(1000, 1000)

    def test_modal_dialogs(browser):
        modal_dialogs_page = DialogsPage(browser)
        modal_dialogs_page.visit()
        modal_dialogs_page.btn_small_modal.click()
    time.sleep(2)
    assert modal_dialogs_page.alert()
    modal_dialogs_page.btn_small_modal.click()
    assert not modal_dialogs_page.alert()