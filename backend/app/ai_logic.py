import os
from google import genai
from dotenv import load_dotenv


load_dotenv()

# Настройка прокси для Псифона
# os.environ['HTTPS_PROXY'] = "http://127.0.0.1:8080"
# os.environ['HTTP_PROXY'] = "http://127.0.0.1:8080"

# Инициализируем клиента
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY"),
    vertexai=False
)

MODELS_PRIORITY = [
    'models/gemini-2.5-flash',      # Приоритет №1: Мощь + Скорость
    'models/gemini-2.0-flash-lite', # Приоритет №2: Легкая и стабильная
    'models/gemini-1.5-flash'       # Приоритет №3: Резерв
]

def ask_gemini(prompt: str):
    for model_id in MODELS_PRIORITY:
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=prompt
            )
            # Возвращаем кортеж: (текст, имя_модели)
            return response.text, model_id
            
        except Exception as e:
            if "429" in str(e) or "404" in str(e):
                continue
            return f"Ошибка AI: {str(e)}", "none"

    return "Все модели заняты", "none"