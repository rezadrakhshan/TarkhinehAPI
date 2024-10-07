from fastapi import FastAPI
from db import models
from db.database import engine
from router import food,authentication

app = FastAPI(title="Tarkhineh")

app.include_router(food.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(bind=engine)
