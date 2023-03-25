from pages.demoqa import DemoQa

    def test_page_elements(browser):
        elements_page = ElementsPage(browser)

        elements_page.visit()


        assert elements_page.test_page_elements.get_text () == "Elements"
        assert elements_page.icon.exist()
        assert elements_page.btn_sidebar_first.exist()
        assert elements_page.btn_sidebarbtn_sidebar_first.exist()

#https://demoqa.com/elements
#app > div > div > div.row > div.col-12.mt-4.col-md-6
#string center Please select an item from left to start practice.


