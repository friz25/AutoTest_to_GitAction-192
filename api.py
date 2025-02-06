import requests
import time, os, dotenv
dotenv.load_dotenv()


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


def test_get_object():
   obj_id = 'ff808181932badb60194dcbba7995d3a'
   responce = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
   # print(f"responce: {responce}")
   assert responce['id'] == obj_id


def test_update_object():
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
      'https://api.restful-api.dev/objects/ff808181932badb60194dcbba7995d3a',
      json=payload
   ).json()
   # print(f"responce: {responce}")
   assert responce['name'] == payload['name']


def test_delete_object():
   obj_id = 'ff808181932badb60194dcbba7995d3a'
   responce = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
   # print(f"responce: {responce}")
   assert responce.status_code == 200
   responce = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
   assert responce.status_code == 404
