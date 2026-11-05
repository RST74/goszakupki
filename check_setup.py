"""Разовая проверка окружения: Telegram-бот + Supabase. Запуск: python check_setup.py"""
import requests
from supabase import create_client
import config
from logger import logger


def test_telegram() -> bool:
    if not config.TELEGRAM_BOT_TOKEN or not config.TELEGRAM_CHAT_ID:
        logger.warning("Telegram: не заданы TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID")
        return False
    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
    r = requests.post(
        url,
        json={
            "chat_id": config.TELEGRAM_CHAT_ID,
            "text": "✅ Тест: мониторинг госзакупок настроен",
        },
        timeout=10,
    )
    if r.ok:
        logger.info("Telegram: тестовое сообщение отправлено")
        return True
    logger.error(f"Telegram: HTTP {r.status_code} {r.text[:200]}")
    return False


def test_supabase() -> bool:
    if not config.SUPABASE_URL or not config.SUPABASE_SERVICE_KEY:
        logger.warning("Supabase: не заданы SUPABASE_URL или SUPABASE_SERVICE_KEY")
        return False
    try:
        # Клиент создаётся, если URL/ключ в правильном формате
        _ = create_client(config.SUPABASE_URL, config.SUPABASE_SERVICE_KEY)
        # Проверяем реальный доступ к REST API
        r = requests.get(
            f"{config.SUPABASE_URL}/rest/v1/",
            headers={
                "apikey": config.SUPABASE_SERVICE_KEY,
                "Authorization": f"Bearer {config.SUPABASE_SERVICE_KEY}",
            },
            timeout=10,
        )
        if r.status_code == 200:
            logger.info("Supabase: ключ валиден, соединение OK")
            return True
        logger.error(f"Supabase: HTTP {r.status_code} {r.text[:200]}")
        return False
    except Exception as e:
        logger.error(f"Supabase: ошибка {e}")
        return False


if __name__ == "__main__":
    logger.info("=== Проверка окружения ===")
    ok_tg = test_telegram()
    ok_sb = test_supabase()
    if ok_tg and ok_sb:
        logger.success("Всё настроено ✅")
    else:
        logger.warning(f"Telegram={ok_tg}, Supabase={ok_sb}")