import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Настройка прокси для Псифона
proxy_url = "http://127.0.0.1:8080"
os.environ['HTTPS_PROXY'] = proxy_url
os.environ['HTTP_PROXY'] = proxy_url

# Инициализируем клиента с ПРАВИЛЬНЫМ названием параметра
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY"),
    vertexai=False  # Теперь без подчеркивания
)

def run():
    print("--- Проверка доступа к Google AI Studio ---")
    try:
        # Получаем список моделей, которые доступны твоему API-ключу
        print("Запрашиваю список моделей...")
        available_models = list(client.models.list())
        
        if not available_models:
            print("Список моделей пуст. Проверь API-ключ в .env!")
            return

        print(f"Доступно моделей: {len(available_models)}")
        
        # Берем самую первую модель из списка (обычно это 1.5-flash или 2.0-flash)
        first_model = available_models[0].name
        print(f"Пробую самую стабильную модель: {first_model}...")

        response = client.models.generate_content(
            model=first_model,
            contents="Если ты видишь это сообщение через прокси, ответь 'Связь в норме!'"
        )
        
        print("\n--- ОТВЕТ GEMINI ---")
        print(response.text)
        print("--------------------")

    except Exception as e:
        print(f"\nОшибка: {e}")
        print("\nПодсказка: Если снова 404, проверь, не пустой ли GOOGLE_API_KEY в .env")

if __name__ == "__main__":
    run()