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
# from loguru import logger as logger_loguru

# logger_loguru.add(
#    "logs/loguru.log", format='{time} {level} {message}',
#    level='INFO', rotation='10 KB', compression='zip'
# )# *можно указать serialize=True и логфайл будет в формате .json

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
   level='INFO', rotation='10 KB', compression='zip'
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

@logger_loguru.catch
def create_object():
   payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": os.getenv('POST_PARAM1'),
         "price": os.getenv('POST_PARAM2'),
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
   responce = requests.post('https://api.restful-api.dev/objects', json=payload).json()
   return responce['id']

@logger_loguru.catch
def test_create_object():
   payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": os.getenv('POST_PARAM1'),
         "price": os.getenv('POST_PARAM2'),
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
   responce = requests.post('https://api.restful-api.dev/objects', json=payload).json()
   # print(f"responce: {responce}")
   assert responce['name'] == payload['name']

@logger_loguru.catch
def test_get_object():
   obj_id = create_object()
   responce = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
   # print(f"responce: {responce}")
   assert responce['id'] == obj_id

@logger_loguru.catch
def test_update_object():
   obj_id = create_object()
   payload = {
         "name": "Apple MacBook Pro 16",
         "data": {
            "year": os.getenv('PUT_PARAM1'),
            "price": os.getenv('PUT_PARAM2'),
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
         }
      }
   responce = requests.put(
      f'https://api.restful-api.dev/objects/{obj_id}',
      json=payload
   ).json()
   # print(f"responce: {responce}")
   assert responce['name'] == payload['name']

@logger_loguru.catch
def test_delete_object():
   obj_id = create_object()
   responce = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
   # print(f"responce: {responce}")
   assert responce.status_code == 200
   responce = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
   assert responce.status_code == 404
