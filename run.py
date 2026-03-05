import uvicorn
import sys
import os

# Добавляем backend в пути, чтобы было видно папку app
sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

if __name__ == "__main__":
    # Убираем пока reload_dirs, оставим просто reload
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)