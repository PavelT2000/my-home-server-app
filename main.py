from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/author")
async def author(request: Request):
    return templates.TemplateResponse("author.html", {"request": request})

@app.get("/work")
async def work(request: Request):
    return templates.TemplateResponse("work.html", {"request": request})