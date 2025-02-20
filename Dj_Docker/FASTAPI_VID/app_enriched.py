from fastapi import FastAPI
import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider


# Initialise OTEL
provider = TracerProvider()
# Sets the global default tracer provider
trace.set_tracer_provider(provider)
# Creates a tracer from the global tracer provider
tracer = trace.get_tracer(__name__)
# Done initialising OTEL

app = FastAPI()

@app.get("/")
def get_homepage():
    count = 1
    while count <= 3:
        with tracer.start_as_current_span(f'loop-count-{count}') as span:
            # print(f'Loop count {count}')
            count += 1
            time.sleep(1)

    return {
        "status": "ok",
        "foo": "bar"
    }

"""
Чтоб запустить
uvicorn --reload app:app
opentelemetry-instrument --service_name my.first.api uvicorn app_enriched:app

Проверить = http://127.0.0.1:8000 
Swagger = http://127.0.0.1:8000/docs
Redoc = http://127.0.0.1:8000/redoc

Jaeger (трейсинг) = http://localhost:16686/
*тут указать "my.first.api"

=======================
# скомпилируем/преобразуем docker-compose.yml в k8s формат/проект
1)kompose convert --out k8s/
# развернём локальный кластер kubernetes
2)kind create cluster --config kind-config.yml
======kind-config.yml======
apiVersion: kind.x-k8s.io/v1alpha4
kind: Cluster
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 30000
    hostPort: 30000
    listenAddress: "0.0.0.0" # Optional, defaults to "0.0.0.0"
    protocol: tcp # Optional, defaults to tcp
- role: worker
=================================
# добавим docker-image нашего app в кластер kind/k8s
3)kind load docker-image bun-wish-list
# создадим k8s ресурсы используя k8s cli (kubectl)
4)kubectl apply -f k8s/
# увидим "ресурсы" нашего k8s кластера
kubectl get all

# Итог: bug: один app не поднялся + порты не exposed
# увидим все контейнеры доступные нашему k8s кластеру
docker exec -it kind-control-plane crictl images
#=== изменили строку в конфиге k8s ====
# применим изменённый конфиг
kubectl apply -f ./k8s/bun-wish-list-deployment.yaml
# еще раз увидим/проверим "ресурсы" нашего k8s кластера
kubectl get all
#=== изменили строку в конфиге nginx (нашего k8s) ====
# применим изменённый конфиг
kubectl apply -f ./k8s/nginx-service.yaml
# еще раз увидим/проверим "ресурсы" нашего k8s кластера
kubectl get all
# \\ Успех //
"""
