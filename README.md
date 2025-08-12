# Habits-Tracker

Бэкенд SPA приложения для формирования полезных привычек по методике Джеймса Клира с полной Docker-поддержкой
 Возможности

✔ Готовая Docker-сборка (PostgreSQL + Redis + Celery + Celery-beat)
✔ Автоматические миграции при запуске
✔ JWT-аутентификация через DRF
✔ Telegram-ботам
✔ Swagger/ReDoc документация


Запуск через Docker 
1. Настройка окружения 
git clone git@github.com:Dmitry-Nikandrov/Project_5_Trecker_habbits_to_git.git
cd Habits-tracker

2. Создайте .env файл:
ini

PostgreSQL
POSTGRES_DB=habits
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_strong_password

Django

SECRET_KEY=your_django_secret_key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

Celery

CELERY_BROKER_URL=redis://redis:6379/0

Telegram

TELEGRAM_BOT_TOKEN=your_bot_token

3. Запуск системы

docker compose up -d --build


