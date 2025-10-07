"""
Конфигурация для Telegram бота интернет-магазина
(совместима с импортом: from config import BOT_TOKEN, POST_CHANNEL_ID)
"""
import os
import sys

# === Telegram credentials (env overrides) ===
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    sys.stderr.write("❌ TELEGRAM_BOT_TOKEN не задан в переменных окружения!\n")
    sys.exit(1)

POST_CHANNEL_ID = os.getenv("POST_CHANNEL_ID")
if not POST_CHANNEL_ID:
    sys.stderr.write("❌ POST_CHANNEL_ID не задан в переменных окружения!\n")
    sys.exit(1)

# Flask secret key
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
if not FLASK_SECRET_KEY:
    sys.stderr.write("❌ FLASK_SECRET_KEY не задан в переменных окружения!\n")
    sys.exit(1)

# Конфигурация окружения
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = ENVIRONMENT == "development"

# Настройки базы данных
# Поддерживаем оба имени env: DB_PATH (используется в database.py) и DATABASE_PATH
_database_path = os.getenv("DB_PATH") or os.getenv("DATABASE_PATH") or "shop_bot.db"
DATABASE_CONFIG = {
    "path": _database_path,
    "backup_interval": 3600,  # Резервное копирование каждый час
    "max_connections": 10,
}

# Настройки безопасности
SECURITY_CONFIG = {
    "rate_limit_per_minute": int(os.getenv("RATE_LIMIT", "20")),
    "max_failed_attempts": 5,
    "block_duration_hours": 24,
    "jwt_secret": os.getenv("JWT_SECRET"),
    "encryption_key": os.getenv("ENCRYPTION_KEY"),
}

# Настройки логирования
LOGGING_CONFIG = {
    "level": os.getenv("LOG_LEVEL", "INFO"),
    "file": os.getenv("LOG_FILE", "bot.log"),
    "max_size": 10 * 1024 * 1024,  # 10MB
    "backup_count": 5,
}

# Настройки Redis (для кэширования)
REDIS_CONFIG = {
    "host": os.getenv("REDIS_HOST", "localhost"),
    "port": int(os.getenv("REDIS_PORT", "6379")),
    "db": int(os.getenv("REDIS_DB", "0")),
    "password": os.getenv("REDIS_PASSWORD"),
    "enabled": os.getenv("REDIS_ENABLED", "false").lower() == "true",
}

# Настройки мониторинга
MONITORING_CONFIG = {
    "health_check_interval": 60,
    "metrics_enabled": True,
    "sentry_dsn": os.getenv("SENTRY_DSN"),
    "prometheus_port": int(os.getenv("PROMETHEUS_PORT", "8000")),
}

# Настройки бота
BOT_CONFIG = {
    "name": os.getenv("BOT_NAME", "Shop Bot"),
    "version": "1.0",
    "description": "Телеграм-бот для интернет-магазина",
    "bot_username": os.getenv("BOT_USERNAME", "YourBot"),
    "currency": os.getenv("CURRENCY", "USD"),
    "currency_symbol": os.getenv("CURRENCY_SYMBOL", "$"),
    "webhook_url": os.getenv("WEBHOOK_URL"),
    "webhook_secret": os.getenv("WEBHOOK_SECRET"),
    "max_message_length": 4096,
    "request_timeout": 30,
    "admin_telegram_id": os.getenv("ADMIN_TELEGRAM_ID"),
    "admin_name": os.getenv("ADMIN_NAME", "Admin"),
    "post_channel_id": POST_CHANNEL_ID,
}

# Контактная информация
CONTACT_INFO = {
    "support_phone": os.getenv("SUPPORT_PHONE", "+000000000"),
    "support_telegram": os.getenv("SUPPORT_TELEGRAM", "@YourSupportBot"),
    "call_center_phone": os.getenv("CALL_CENTER_PHONE", "+000000000"),
    "working_hours": os.getenv("WORKING_HOURS", "9:00 - 18:00 (Пн-Пт)"),
}

# Сообщения бота
MESSAGES = {
    "welcome_new": """
🛍 <b>Добро пожаловать в наш интернет-магазин!</b>

Здесь вы можете:
• 📱 Просматривать каталог товаров
• 🛒 Добавлять товары в корзину  
• 📦 Оформлять заказы
• 📋 Отслеживать статус доставки

Для начала работы пройдите быструю регистрацию.
    """,

    "welcome_back": """
👋 <b>С возвращением!</b>

Рады видеть вас снова в нашем магазине.
Выберите действие из меню ниже:
    """,

    "help": """
ℹ️ <b>Справка по использованию бота:</b>

🛍 <b>Каталог</b> - просмотр товаров по категориям
🛒 <b>Корзина</b> - ваши выбранные товары
📋 <b>Мои заказы</b> - история ваших покупок
👤 <b>Профиль</b> - управление вашими данными

<b>Как сделать заказ:</b>
1️⃣ Выберите товары в каталоге
2️⃣ Добавьте их в корзину
3️⃣ Перейдите в корзину и оформите заказ
4️⃣ Укажите адрес и способ оплаты

❓ По вопросам обращайтесь к администратору.
    """,

    "registration_complete": """
✅ <b>Регистрация завершена!</b>

Добро пожаловать в наш магазин! 🎉

Теперь вы можете:
• Просматривать каталог товаров
• Добавлять товары в корзину
• Оформлять заказы

Приятных покупок! 🛍
    """,

    "empty_cart": """
🛒 <b>Ваша корзина пуста</b>

Перейдите в каталог, чтобы добавить товары!
    """,

    "order_success": """
✅ <b>Заказ успешно оформлен!</b>

📞 Мы свяжемся с вами в ближайшее время для подтверждения.

Спасибо за покупку! 🎉
    """,
}

# Статусы заказов
ORDER_STATUSES = {
    "pending": "⏳ В обработке",
    "confirmed": "✅ Подтвержден",
    "shipped": "🚚 Отправлен",
    "delivered": "📦 Доставлен",
    "cancelled": "❌ Отменен",
}

# Способы оплаты
PAYMENT_METHODS = {
    "online": "💳 Онлайн оплата",
    "cash": "💵 Наличными при получении",
}

# Эмодзи для категорий
CATEGORY_EMOJIS = {
    "Электроника": "📱",
    "Одежда": "👕",
    "Дом и сад": "🏠",
    "Спорт": "⚽",
    "Книги": "📚",
    "Красота": "💄",
}

# Настройки пагинации
PAGINATION = {
    "products_per_page": 5,
    "orders_per_page": 10,
}

__all__ = [
    "BOT_TOKEN",
    "POST_CHANNEL_ID",
    "FLASK_SECRET_KEY",
    "ENVIRONMENT",
    "DEBUG",
    "DATABASE_CONFIG",
    "SECURITY_CONFIG",
    "LOGGING_CONFIG",
    "REDIS_CONFIG",
    "MONITORING_CONFIG",
    "BOT_CONFIG",
    "CONTACT_INFO",
    "MESSAGES",
    "ORDER_STATUSES",
    "PAYMENT_METHODS",
    "CATEGORY_EMOJIS",
    "PAGINATION",
]
