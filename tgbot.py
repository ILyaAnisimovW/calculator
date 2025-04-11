import requests

token = ""
chat_id = ""

# ASCII-арт для Telegram
ascii_art = "0_0"

# URL Telegram API
url = f"https://api.telegram.org/bot{token}/sendMessage"

# Тело запроса
payload = {
    "chat_id": chat_id,
    "text": ascii_art
}

# Отправка
response = requests.post(url, json=payload)

# Проверка ответа
if response.status_code != 200:
    print("❌ Ошибка:", response.text)
else:
    print("✅ Отправлено!")
