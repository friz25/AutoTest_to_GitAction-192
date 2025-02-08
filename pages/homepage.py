from selenium.webdriver.common.by import By
import allure

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        with allure.step('Открыли Главную страницу'):
            self.browser.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self):
        with allure.step('Кликнули по "Samsung galaxy s6"'):
            galaxy_s6 = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
            galaxy_s6.click()

    def click_monitor(self):
        with allure.step('Кликнули на категорию товаров "Monitors"'):
            monitor_link = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
            monitor_link.click()

    def check_that_products_count(self, count):
        with allure.step(f'Убедились что там именно {count} товара'):
            monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
            assert len(monitors) == count
