import os
import uvicorn
from fastapi import FastAPI, Request
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware  # Добавлено
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# 1. ОБЯЗАТЕЛЬНО: Добавляем Middleware для сессий
# secret_key может быть любой строкой, она нужна для шифрования сессии
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "super-secret-key"))

# Загружаем настройки
config = Config(environ={
    'GOOGLE_CLIENT_ID': os.getenv("GOOGLE_CLIENT_ID"),
    'GOOGLE_CLIENT_SECRET': os.getenv("GOOGLE_CLIENT_SECRET")
})

oauth = OAuth(config)
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

@app.get('/login')
async def login(request: Request):
    # Если ты работаешь через прокси или Tailscale, убедись, что redirect_uri 
    # совпадает с тем, что указано в Google Console
    redirect_uri = request.url_for('auth_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@app.get('/auth/callback')
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = token.get('userinfo')
    return {"message": f"Привет, {user['name']}!", "user": user}

# 2. ЗАПУСК ЧЕРЕЗ UVICORN
if __name__ == "__main__":
    # host="0.0.0.0" — чтобы было видно в сети (Tailscale)
    # port=8000 — стандартный порт для FastAPI
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)