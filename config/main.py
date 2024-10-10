from fastapi import FastAPI,Request
from db import models
from db.database import engine
from router import food, authentication, branch
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Tarkhineh",docs_url=None)

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


app.include_router(food.router)
app.include_router(authentication.router)
app.include_router(branch.router)

models.Base.metadata.create_all(bind=engine)
