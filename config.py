"""Конфигурация проекта: чтение .env, фильтры, константы."""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def _str(name: str, default: str = "") -> str:
    return (os.getenv(name) or default).strip()


def _int(name: str, default: int) -> int:
    """Пустое значение в .env (например, `PARSER_DEPTH=`) не роняет программу."""
    value = _str(name)
    return int(value) if value else default


def _float(name: str, default: float) -> float:
    value = _str(name)
    return float(value) if value else default


# --- Telegram ---
TELEGRAM_BOT_TOKEN = _str("TELEGRAM_BOT_TOKEN")
# Строка, а не int: Telegram принимает и числовой id (в т.ч. отрицательный у групп),
# и @username канала
TELEGRAM_CHAT_ID = _str("TELEGRAM_CHAT_ID")

# --- Supabase ---
SUPABASE_URL = _str("SUPABASE_URL").rstrip("/")
SUPABASE_ANON_KEY = _str("SUPABASE_ANON_KEY")        # только для приложения (чтение)
SUPABASE_SERVICE_KEY = _str("SUPABASE_SERVICE_KEY")  # только для сборщика, никому не передавать

# --- Сайт ---
BASE_URL = "https://goszakupki.by"

# --- Парсер ---
PARSER_DEPTH = _int("PARSER_DEPTH", 5)            # сколько страниц списка обходить
REQUEST_TIMEOUT = _int("REQUEST_TIMEOUT", 30)     # секунды
REQUEST_DELAY_MIN = _float("REQUEST_DELAY_MIN", 2)
REQUEST_DELAY_MAX = _float("REQUEST_DELAY_MAX", 5)
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) GoszakupkiMonitor/1.0"

if REQUEST_DELAY_MIN > REQUEST_DELAY_MAX:
    raise ValueError("REQUEST_DELAY_MIN не может быть больше REQUEST_DELAY_MAX")

# --- Пути ---
LOGS_DIR = BASE_DIR / "logs"
REPORTS_DIR = BASE_DIR / "reports"
SAMPLES_DIR = BASE_DIR / "samples"

# --- Фильтры уведомлений (заполним на 8-й день) ---
FILTER_KEYWORDS: list[str] = []
FILTER_EXCLUDE: list[str] = []
FILTER_REGIONS: list[str] = []
FILTER_AMOUNT_MIN = 0
FILTER_AMOUNT_MAX = 10**12
