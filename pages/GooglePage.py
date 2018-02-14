from selenium.webdriver.common.by import By
from BasePage import BasePage

class GooglePage(BasePage):

    def __init__(self, browser, page):
        BasePage.__init__(
            self, 
            browser,
            page
        )
        self.browser.get(page)

    locator = {
        "SEARCH_BOX": (By.ID, 'lst-ib'),
        "SUBMIT_BTN": (By.XPATH, '//input[@value="Google Search"]')
    }

    def search(self, search_term):
        self.browser.find_element(*self.locator['SEARCH_BOX']).send_keys(search_term)
        self.browser.find_element(*self.locator['SUBMIT_BTN']).click()