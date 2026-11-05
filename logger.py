"""Настройка логирования через loguru: консоль + файлы в logs/ с ротацией."""
import sys
from loguru import logger
from config import LOGS_DIR

LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Убираем стандартный обработчик loguru
logger.remove()

# Вывод в консоль
logger.add(
    sys.stderr,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
)

# Запись в файл: новый файл каждый день, хранить 30 дней, старые сжимаются в zip
logger.add(
    LOGS_DIR / "app_{time:YYYY-MM-DD}.log",
    level="DEBUG",
    rotation="00:00",
    retention="30 days",
    compression="zip",
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
)

__all__ = ["logger"]