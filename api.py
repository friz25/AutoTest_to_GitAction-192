import requests
import time, os, dotenv
dotenv.load_dotenv()


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
   print(f"responce: {responce}")


def get_object():
   responce = requests.get('https://api.restful-api.dev/objects/ff808181932badb60194dcbba7995d3a').json()
   print(f"responce: {responce}")


def update_object():
   payload = {
         "name": "Apple MacBook Pro 16",
         "data": {
            "year": os.getenv('PUT_PARAM1'),
            "price": os.getenv('PUT_PARAM2'),
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
         }
      }
   responce = requests.put('https://api.restful-api.dev/objects/ff808181932badb60194dcbba7995d3a', json=payload).json()
   print(f"responce: {responce}")


def delete_object():
   responce = requests.delete('https://api.restful-api.dev/objects/ff808181932badb60194dcbba7995d3a').json()
   print(f"responce: {responce}")
