from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
def get_homepage():
    count = 1
    while count <= 3:
        print(f'Loop count {count}')
        count += 1
        time.sleep(1)

    return {
        "status": "ok",
        "foo": "bar"
    }

"""
Чтоб запустить
uvicorn --reload app:app
opentelemetry-instrument --service_name my.first.api uvicorn app:app

Проверить = http://127.0.0.1:8000 
Swagger = http://127.0.0.1:8000/docs
Redoc = http://127.0.0.1:8000/redoc
"""
