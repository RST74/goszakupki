"""Конфигурация проекта: чтение .env, фильтры, константы."""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# --- Telegram ---
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID", "0"))

# --- Supabase ---
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY", "")

# --- Парсер ---
PARSER_DEPTH = int(os.getenv("PARSER_DEPTH", "5"))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))
REQUEST_DELAY_MIN = int(os.getenv("REQUEST_DELAY_MIN", "2"))
REQUEST_DELAY_MAX = int(os.getenv("REQUEST_DELAY_MAX", "5"))
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) GoszakupkiMonitor/1.0"

# --- Пути ---
LOGS_DIR = BASE_DIR / "logs"
REPORTS_DIR = BASE_DIR / "reports"
SAMPLES_DIR = BASE_DIR / "samples"

# --- Фильтры уведомлений (заполним позже) ---
FILTER_KEYWORDS: list[str] = []
FILTER_EXCLUDE: list[str] = []
FILTER_REGIONS: list[str] = []
FILTER_AMOUNT_MIN = 0
FILTER_AMOUNT_MAX = 10**12