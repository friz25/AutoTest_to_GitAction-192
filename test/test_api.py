#====189 API===================== ГОТОВО
# https://restful-api.dev/
#====//189 API=====================
import requests
import pytest
import time, os, dotenv, logging
from loguru import logger as logger_loguru
dotenv.load_dotenv()

# region === ЛОГ / СПОСОБ 1 ===
# import logging

# logging.basicConfig(
#    level=logging.DEBUG, filename='logs/logging.log',
#    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
#    datefmt='%d/%m/%Y %I:%M:%S', encoding='utf-8', filemode='w'
# )
#
# logging.debug('Дебаг')
# logging.info('Инфо')
# logging.warning('Варнинг')
# logging.error('Эррор')
# logging.critical('Критикал')
#
# try:
#    10/0
# except Exception as e:
#    logging.exception(e)

# endregion
# region === ЛОГ / СПОСОБ 2 (черep Handler) ====
# import logging

# logger = logging.getLogger(__name__)
# logger.level = logging.INFO
# # handler = logging.FileHandler(f'logs/{__name__}.log', encoding='utf-8', mode='w')
# handler = logging.FileHandler(f'logs/logger.log', encoding='utf-8', mode='w')
# formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')
# handler.setFormatter(formatter)
# logger.addHandler(handler)


# logger.info('Давай протестируем файл на данные?')

# endregion
# region === ЛОГ / СПОСОБ 3 (через pip LOGURU) ====
from loguru import logger as logger_loguru

logger_loguru.add(
   "logs/loguru.log", format='{time} {level} {message}',
   level='INFO', rotation='10 KB', compression='zip',
)# *можно указать serialize=True и логфайл будет в формате .json

# logger_loguru.info('Давай протестируем файл на данные?')

#тест на ротацию
# for _ in range(1000):
#    logger_loguru.info("Hello, World (debug)!")

# крутой ловец ошибок
# @logger_loguru.catch
# def main():
#    1/0
#
# main()

# endregion

# region === ЛОГ / СПОСОБ 3 (через pip LOGURU) ====

logger_loguru.add(
   "logs/loguru.log", format='{time} {level} {message}',
   level='ERROR', rotation='10 MB', compression='zip'
)
# *можно указать serialize=True и логфайл будет в формате .json

# logger_loguru.info('Давай протестируем файл на данные?')

#тест на ротацию
# for _ in range(1000):
#    logger_loguru.info("Hello, World (debug)!")

#крутой ловец ошибок
# @logger_loguru.catch
# def main():
#    1/0
#
# main()

# endregion

# region === 189 API ===
# @logger_loguru.catch
# @pytest.fixture()
# def obj_id():
#    payload = {
#       "name": "Apple MacBook Pro 16",
#       "data": {
#          "year": os.getenv('POST_PARAM1'),
#          "price": os.getenv('POST_PARAM2'),
#          "CPU model": "Intel Core i9",
#          "Hard disk size": "1 TB"
#       }
#    }
#    responce = requests.post('https://api.restful-api.dev/objects', json=payload).json()
#    yield responce['id']
#    requests.delete(f'https://api.restful-api.dev/objects/{responce["id"]}')
#
# @logger_loguru.catch
# def test_create_object():
#    payload = {
#       "name": "Apple MacBook Pro 16",
#       "data": {
#          "year": os.getenv('POST_PARAM1'),
#          "price": os.getenv('POST_PARAM2'),
#          "CPU model": "Intel Core i9",
#          "Hard disk size": "1 TB"
#       }
#    }
#    responce = requests.post('https://api.restful-api.dev/objects', json=payload).json()
#    # print(f"responce: {responce}")
#    assert responce['name'] == payload['name']
#
# @logger_loguru.catch
# def test_get_object(obj_id):
#    # print(obj_id) #ручной тест (что обьект (после yield) реал удаляеться)
#    responce = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
#    # print(f"responce: {responce}")
#    assert responce['id'] == obj_id
#
# @logger_loguru.catch
# def test_update_object(obj_id):
#    payload = {
#          "name": "Apple MacBook Pro 16",
#          "data": {
#             "year": os.getenv('PUT_PARAM1'),
#             "price": os.getenv('PUT_PARAM2'),
#             "CPU model": "Intel Core i9",
#             "Hard disk size": "1 TB"
#          }
#       }
#    responce = requests.put(
#       f'https://api.restful-api.dev/objects/{obj_id}',
#       json=payload
#    ).json()
#    # print(f"responce: {responce}")
#    assert responce['name'] == payload['name']
#
# @logger_loguru.catch
# def test_delete_object(obj_id):
#    responce = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
#    # print(f"responce: {responce}")
#    assert responce.status_code == 200
#    responce = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
#    assert responce.status_code == 404

# endregion
# https://restful-api.dev/

# region ====190/191 системные перем + dotenv / тестим сайт MAGENTO =====
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # @logger_loguru.catch
# def test_login():
#    login = os.getenv('MY_LOGIN')
#    password = os.getenv('MY_PASS')
#    # driver = webdriver.Firefox() #не работает (нет Firefox драйвера видимо)
#    # driver = webdriver.Firefox()
#    driver = webdriver.Chrome()
#
#    driver.maximize_window()
#    driver.get('https://magento.softwaretestingboard.com/customer/account/login/')
#    login_field = driver.find_element(By.CSS_SELECTOR, '#email')
#    pass_field = driver.find_element(By.CSS_SELECTOR, '#pass')
#    login_field.send_keys(login)
#    pass_field.send_keys(password)
#    time.sleep(2)
#
#    driver.close()
#    driver.quit()

# endregion
# https://magento.softwaretestingboard.com/

from pages.homepage import HomePage
from pages.product import ProductPage

# region === 192 ОСНОВНОЙ в GitActions / тестим сайт DemoBLAZE ======

# region Первая часть теста

# import pytest

# @pytest.fixture()
# def before_after():
#     # print('\nBefore test')
#     logger_loguru.info('Before test')
#     yield
#     # print('\nAfter test')
#     logger_loguru.info('After test')
#
# def test_demo1():
#    assert 1 == 1
#
# def test_demo2(before_after):
#     assert 2 == 3

# endregion
# region 2я часть теста

def test_open_s6(browser):
   """no homo"""
   homepage = HomePage(browser)
   homepage.open()
   homepage.click_galaxy_s6()
   product_page = ProductPage(browser)
   product_page.check_title_is('Samsung galaxy s6')

def test_two_monitors(browser):
   homepage = HomePage(browser)
   homepage.open()
   homepage.click_monitor()
   time.sleep(5)
   homepage.check_that_products_count(2)


# endregion

# endregion
# https://demoblaze.com/

#====193 Создание POM проекта / тестим QA-PRACTICE.COM =======
# qa-practice.com

#====194 ALLURE / тоже QA-PRACTICE.COM======
# qa-practice.com

#====195 ALLURE в GitActions========

#====199 Оповещение в SCLAK и TELEGRAM========



