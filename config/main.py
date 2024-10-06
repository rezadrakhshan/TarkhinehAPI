from fastapi import FastAPI
from db import models
from db.database import engine
from router import food

app = FastAPI(title="Tarkhineh")

app.include_router(food.router)

models.Base.metadata.create_all(bind=engine)
