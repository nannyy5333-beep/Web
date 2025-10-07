#!/usr/bin/env python3
"""
Инициализация базы данных.
Создаёт все таблицы и тестовые данные.
"""
import os
import sys

# Проверяем наличие DATABASE_URL
if not os.getenv("DATABASE_URL"):
    sys.stderr.write("❌ DATABASE_URL не задан! Задайте переменную окружения.\n")
    sys.exit(1)

from database import DatabaseManager

if __name__ == "__main__":
    print("🔄 Инициализация базы данных...")
    db = DatabaseManager()
    print("✅ База данных инициализирована!")
