import time
from pages.formpage import FormPage

def test_login_form (browser):
    formpage = FormPage(browser)
    formpage.visit()
    assert not formpage.modal_dialog.exist()
    time.sleep(2)
    formpage.first_name.send_keys('Саша')
    formpage.last_name.send_keys('Попкова')
    formpage.user_email.send_keys('ыввв@dsvsdv.ff')
    formpage.gender_radio_1.click_force()
    formpage.user_number.send_keys('2568497')
    time.sleep(2)
    formpage.btn_submit.click_force()
    time.sleep(2)
    assert formpage.modal_dialog.exist()
    formpage.btn_close_modal.click_force()