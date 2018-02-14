from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage(object):

    def __init__(self, browser, page=''):
        self.browser = browser
        self.page = page

    def get_page(self):
        return self.page