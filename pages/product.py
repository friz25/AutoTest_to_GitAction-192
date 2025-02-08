from selenium.webdriver.common.by import By
import allure

class ProductPage:

    def __init__(self, browser):
        with allure.step('Открыли страницу товара'):
            self.browser = browser

    def check_title_is(self, title):
        with allure.step(f'Убедились что там (действительно) "{title}"'):
            page_title = self.browser.find_element(By.CSS_SELECTOR, 'h2')
            assert page_title.text == title
