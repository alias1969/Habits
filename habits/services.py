import requests

from config import settings


def telegram_message(chat_id, message):
    """Отправка сообщений в Телеграм."""
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
        params=params,
    )
