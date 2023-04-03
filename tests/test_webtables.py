from pages.webtables_page import WebtablesPage
import time

def test_webtables(browser):
    webtables_page = WebtablesPage(browser)
    webtables_page.visit()
    webtables_page.btn_add.click()
    assert not webtables_page.btn_submit.click()
    assert webtables_page.redist_form_modal.visible()
def test_webtables (browser):
    webtables_page = WebtablesPage(browser)
    webtables_page.visit()
    webtables_page.btn_add.click()
    assert not webtables_page.btn_submit.click()
    assert webtables_page.redist_form_modal.exist()
    time.sleep(2)
    webtables.first_name.send_keys('Саша')
    webtables.last_name.send_keys('Попкова')
    webtables.user_email.send_keys('ыввв@dsvsdv.ff')
    webtables.age.send_keys('11')
    webtables.salaty.send_keys('10')
    webtables.department.send_keys('10')
    time.sleep(2)
    webtables.btn_submit.click_force()
    time.sleep(2)
    assert webtables_page.redist_form_modal.exist()
    webtables_page.btn_submit.click_force()
    assert webtables_page.reacttable.exist.str ('Саша', 'Попкова', 'ыввв@dsvsdv.ff', '11',' 10', '10')



def test_webtables1(browser):
    webtables_page = WebtablesPage(browser)
    webtables_page.visit()
    time.sleep(2)
    webtables_page.btn_count_str.scroll_element()
    webtables_page.inp_count_str.send_keys('5 строк')
    webtables_page.inp_count_str.send_keys(Keys.ENTER)
    time.sleep(2)
    webtables_page.btn_next.click()
    webtables_page.btn_previus.click()
    assert webtables_page.btn_next.exist('desable')
    assert webtables_page.btn_previus.exist('desable')