# Мониторинг закупок goszakupki.by

Каждый час с 09:00 до 18:00 собирает опубликованные закупки с [goszakupki.by](https://goszakupki.by),
сохраняет их в базу (Supabase), строит Excel-отчёт и присылает уведомления в Telegram.

## Статус

| День | Модуль | Что | Статус |
|---|---|---|---|
| 1 | М0 | Окружение, конфиг, логи, проверка Telegram и Supabase | ✅ |
| 2 | М1 | Исследование сайта, образцы страниц в `samples/` | ⏳ |
| 3 | М2 | Схема БД (`schema.sql`) и `repository.py` | ⬜ |
| 4–5 | М1 | `fetcher.py`, `parser.py`, `models.py` | ⬜ |
| 6 | М3 | Оркестратор `main.py` | ⬜ |
| 7 | М4 | Excel-отчёт `report.py` | ⬜ |
| 8 | М5 | Уведомления | ⬜ |
| 9 | М6 | Планировщик Windows | ⬜ |
| 10–14 | М7 | Android-приложение | ⬜ |
| 15 | М8 | Тесты и документация | ⬜ |

## Установка (Windows)

Нужен **Python 3.11+** (рекомендуется 3.12). Проверить: `py -0p`.

```powershell
git clone https://github.com/RST74/goszakupki.git
cd goszakupki
py -3.12 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Заполните `.env`:

| Переменная | Где взять |
|---|---|
| `TELEGRAM_BOT_TOKEN` | @BotFather → `/newbot` |
| `TELEGRAM_CHAT_ID` | написать боту любое сообщение, открыть `https://api.telegram.org/bot<TOKEN>/getUpdates`, взять `chat.id` |
| `SUPABASE_URL`, ключи | Supabase → Project Settings → API |
| `PARSER_DEPTH` | сколько страниц списка обходить за запуск (по умолчанию 5) |
| `REQUEST_DELAY_MIN/MAX` | пауза между запросами к сайту, секунды |

Проверка:

```powershell
python check_setup.py   # придёт тестовое сообщение в Telegram
pytest                  # автотесты
```

## Структура

```
config.py        настройки из .env, фильтры
logger.py        логи: консоль + logs/app_ГГГГ-ММ-ДД.log (хранятся 30 дней)
check_setup.py   проверка Telegram и Supabase
fetcher.py       загрузка страниц с повторами и паузами        (М1)
parser.py        разбор HTML/JSON в закупки                     (М1)
models.py        модель Tender                                  (М1)
schema.sql       таблицы Supabase                               (М2)
repository.py    запись и чтение БД                             (М2)
report.py        Excel-отчёт                                    (М4)
main.py          точка входа для Планировщика                   (М3)
samples/         сохранённые страницы сайта для тестов
tests/           pytest
```

## Безопасность

- `.env` не коммитится. `SUPABASE_SERVICE_KEY` даёт полный доступ к базе: только для сборщика на ПК.
- В приложение на телефоне идёт только `SUPABASE_ANON_KEY` (чтение, ограничено правилами RLS).
- Сбор данных согласован рапортом; к сайту не чаще одного обхода в час, с паузами между запросами.
