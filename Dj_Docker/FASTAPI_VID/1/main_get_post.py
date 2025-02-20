from fastapi import FastAPI
from pydantic import BaseModel

class MyObject(BaseModel):
    id: str
    name: str
    value: float

app = FastAPI()


@app.get("/")
def get_homepage():
    return { "foo": "bar" }

@app.post("/send")
def send_things(my_object: MyObject):
    return {
        "status": "ok",
        "recieved_object": my_object
    }

"""
Чтоб запустить
uvicorn --reload main_get_post:app

Проверить = http://127.0.0.1:8000 
Swagger = http://127.0.0.1:8000/docs
Redoc = http://127.0.0.1:8000/redoc
"""
