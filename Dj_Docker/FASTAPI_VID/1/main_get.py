from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return { "foo": "bar" }

"""
Чтоб запустить
uvicorn --reload main_get:app

Проверить = http://127.0.0.1:8000 
Swagger = http://127.0.0.1:8000/docs
"""
