rom pages.webtables_page import WebtablesPage
import time

def test_sort(browser):
    webtables_page = WebtablesPage(browser)
    webtables_page.visit()
    namelist =('Cierra', 'Кirrа', 'Alden')
    webtables_page.btn_sort_name.click()
    time.sleep(2)
    namelist2 = ('Alden', 'Cierra', 'Кirrа')
    if namelist == namelist2
        print('сортировка не прошла')
    else:
        print('сортировка прошла')
