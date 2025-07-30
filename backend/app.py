from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Hello World"}

instrumentator = Instrumentator().instrument(app).expose(app)