from fastapi import FastAPI
from db import models
from db.database import engine
from router import food,authentication,branch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Tarkhineh")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(food.router)
app.include_router(authentication.router)
app.include_router(branch.router)

models.Base.metadata.create_all(bind=engine)
