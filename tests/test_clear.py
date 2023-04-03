from pages.text_box import Text_boxPage
import time

def test_clear(browser):
    text_box = Text_boxPage(browser)
    text_box.visit()
    text_box_name.send_keys ('ghjkkl')
    time.sleep(2)
    text_box_name.clear()
    time.sleep(2)
    assert text_box_name.get_text ==' '
