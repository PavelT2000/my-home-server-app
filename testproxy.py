import httpx

# Проверяем SOCKS порт, который ты только что вписал в Псифон
proxy_url = "socks5://127.0.0.1:9050"

try:
    with httpx.Client(proxy=proxy_url, timeout=15.0) as client:
        # Просим сервис сказать, из какой мы страны
        country = client.get("https://ipapi.co/country_name/").text
        print(f"--- РЕЗУЛЬТАТ ---")
        print(f"Страна через Псифон: {country}")
        print(f"------------------")
except Exception as e:
    print(f"Ошибка: Псифон не отвечает на порту 9050. Детали: {e}")