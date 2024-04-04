from fastapi import FastAPI
from routes import router

app = FastAPI()

app.router = router
