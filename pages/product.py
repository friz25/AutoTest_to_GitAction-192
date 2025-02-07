import time
from selenium.webdriver.common.by import By
from pages.homepage import HomePage

class ProductPage:

    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, 'h2')
        assert page_title.text == title
