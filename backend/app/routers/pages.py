import os
from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

router = APIRouter()

# Определяем корень
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

@router.get("/")
async def index(request: Request):
    file_path = TEMPLATES_DIR / "index.html"
    if file_path.exists():
        return FileResponse(str(file_path))
    return {"error": f"Файл не найден по пути: {file_path}"}

@router.get("/author")
async def author(request: Request):
    return FileResponse(str(TEMPLATES_DIR / "author.html"))

@router.get("/work")
async def work(request: Request):
    return FileResponse(str(TEMPLATES_DIR / "work.html"))

@router.get("/commands")
async def commands(request: Request):
    return FileResponse(str(TEMPLATES_DIR / "commands.html"))