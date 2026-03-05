import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Настройка прокси (обязательно, чтобы Google нас пустил)
os.environ['HTTPS_PROXY'] = "http://127.0.0.1:8080"
os.environ['HTTP_PROXY'] = "http://127.0.0.1:8080"

# Инициализируем клиента
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY"),
    vertexai=False
)

def get_all_models():
    print("--- ЗАПРОС СПИСКА МОДЕЛЕЙ ---")
    try:
        # Получаем итерируемый список моделей
        models = client.models.list()
        
        print(f"{'НАЗВАНИЕ (ID)':<40} | {'ОПИСАНИЕ'}")
        print("-" * 80)
        
        for m in models:
            # Выводим техническое имя (которое нужно вставлять в код) и описание
            print(f"{m.name:<40} | {m.description[:40]}...")
            
    except Exception as e:
        print(f"Ошибка при получении списка: {e}")

if __name__ == "__main__":
    get_all_models()