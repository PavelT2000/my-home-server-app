import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import pages, api

app = FastAPI(title="My Home Server AI")

# Четко определяем корень: это папка, где лежит run.py (на два уровня выше этого файла)
# __file__ это backend/app/main.py -> .parent это backend/app -> .parent это backend -> .parent это корень
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 1. Статика (корень/static)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# 2. React Assets (корень/frontend/dist/assets)
react_assets = BASE_DIR / "frontend" / "dist" / "assets"
if react_assets.exists():
    app.mount("/assets", StaticFiles(directory=str(react_assets)), name="assets")
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Маршруты
app.include_router(pages.router)
app.include_router(api.router)

@app.get("/ai")
async def ai_page():
    react_index = BASE_DIR / "frontend" / "dist" / "index.html"
    if react_index.exists():
        return FileResponse(str(react_index))
    return {"error": "React build not found"}

