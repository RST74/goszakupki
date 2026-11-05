"""Конфиг не должен падать на пустых значениях из .env.example."""
import importlib


def test_empty_env_values_use_defaults(monkeypatch):
    for name in ("TELEGRAM_CHAT_ID", "PARSER_DEPTH", "REQUEST_TIMEOUT",
                 "REQUEST_DELAY_MIN", "REQUEST_DELAY_MAX"):
        monkeypatch.setenv(name, "")
    import config
    importlib.reload(config)
    assert config.TELEGRAM_CHAT_ID == ""
    assert config.PARSER_DEPTH == 5
    assert config.REQUEST_DELAY_MAX == 5.0


def test_negative_group_chat_id(monkeypatch):
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "-1001234567890")
    import config
    importlib.reload(config)
    assert config.TELEGRAM_CHAT_ID == "-1001234567890"
