from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.auth import get_current_user
from app.ai_logic import ask_gemini


router = APIRouter(prefix="/api")

# Описываем структуру входящего запроса
class UserRequest(BaseModel):
    prompt: str

class AIResponse(BaseModel):
    answer: str
    model: str  # Добавляем инфо о модели

@router.post("/chat")
async def chat_with_ai(request: UserRequest, user: dict = Depends(get_current_user)):
    # Теперь у нас есть данные пользователя в переменной 'user'
    print(f"Запрос от: {user['email']}")
    
    ai_text, model_used = ask_gemini(request.prompt)
    return {"answer": ai_text, "model": model_used}