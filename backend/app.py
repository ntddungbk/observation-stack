from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from xlogging import Logger


logger = Logger()
app = FastAPI()


@app.get("/healthz")
def health():
    logger.info("Check health")
    return {"status": "ok"}


@app.get("/")
def read_root():
    logger.info("Hello")
    return {"message": "Hello World"}


instrumentator = Instrumentator().instrument(app).expose(app)
