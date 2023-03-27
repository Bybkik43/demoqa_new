from pages.formpage import FormPage
import time
def first_name(browser):
    formpage = FormPage(browser)
    formpage.visit()
    formpage.first_name.send_keys('Саша')
    time.sleep(2)
def last_name(browser):
    formpage = FormPage(browser)
    formpage.visit()
    formpage.last_name.send_keys('Попкова')
    time.sleep(2)
def gender(browser):
    formpage = FormPage(browser)
    formpage.visit()
    formpage.gender.send_keys('female')
    time.sleep(2)
