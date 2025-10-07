# -*- coding: utf-8 -*-
"""Config populated per user's request.
NOTE: Environment variables (if set) override these defaults.
"""
import os

def _env_bool(key: str, default: bool = False) -> bool:
    v = os.getenv(key)
    if v is None:
        return default
    return str(v).strip().lower() in ("1", "true", "yes", "on")

# Telegram bot
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN", "8292684103:AAFEG4KH_exqYeB56BcCxl6_9gODBEoraSQ")
POST_CHANNEL_ID = os.getenv("POST_CHANNEL_ID", "-1002566537425")

# Flask
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "Md4n8uRIO88gVYcZGL9ubWPd61hYcb2hzLCorORJurM")
DEBUG = _env_bool("DEBUG", False)

# Database (optional persistent disk path on Render)
DB_PATH = os.getenv("DB_PATH", None)