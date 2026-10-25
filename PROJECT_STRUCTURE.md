# Структура проекта: Stable-CRM (FastAPI + PostgreSQL + SQLAlchemy)

Этот файл служит памяткой и чек-листом для создания структуры проекта. 
Вы можете отмечать созданные файлы и папки символом `[x]`.

---

## 🌳 Дерево проекта

```text
stable-CRM/
├── .env                              # Локальные переменные окружения (пароли, хосты, ключи JWT)
├── .env.example                      # Пример настроек для других разработчиков и Git
├── .gitignore                        # Игнорируемые файлы (venv, .env, __pycache__)
├── Dockerfile                        # Инструкция сборки контейнера FastAPI
├── docker-compose.yml                # Запуск базы данных PostgreSQL (и приложения)
├── requirements.txt                  # Зависимости проекта
├── README.md                         # Описание проекта
├── alembic.ini                       # Создастся позже автоматически (через команду alembic init)
│
├── app/                              # Основной пакет приложения
│   ├── __init__.py
│   ├── main.py                       # Точка входа: создание FastAPI приложения и подключение роутеров
│   ├── config.py                     # Настройки через pydantic-settings (чтение .env)
│   ├── database.py                   # Подключение к БД, движок, фабрика сессий, базовый класс
│   │
│   ├── core/                         # Безопасность и криптография
│   │   ├── __init__.py
│   │   └── security.py               # Хеширование паролей (bcrypt), генерация и декодирование JWT
│   │
│   ├── models/                       # SQLAlchemy-модели (таблицы в PostgreSQL)
│   │   ├── __init__.py               # Импорт всех моделей для корректной работы Alembic
│   │   ├── user.py                   # Пользователи и роли (ADMIN, MODERATOR, USER)
│   │   ├── horse.py                  # Лошади (кличка, дата рождения/возраст, лимит минут)
│   │   ├── service.py                # Услуги и прокаты (название, длительность, цена)
│   │   └── booking.py                # Записи на прокат (связывает лошадь, услугу, время)
│   │
│   ├── schemas/                      # Pydantic-схемы (валидация входных данных и сериализация ответов)
│   │   ├── __init__.py
│   │   ├── user.py                   # Схемы для пользователя (создание, логин, токен, профиль)
│   │   ├── horse.py                  # Схемы для лошади (создание, редактирование, просмотр)
│   │   ├── service.py                # Схемы для услуг
│   │   └── booking.py                # Схемы для бронирований
│   │
│   ├── crud/                         # Функции прямых запросов к БД (SELECT, INSERT, UPDATE, DELETE)
│   │   ├── __init__.py
│   │   ├── crud_user.py              # Запросы по пользователям
│   │   ├── crud_horse.py             # Запросы по лошадям
│   │   ├── crud_service.py           # Запросы по услугам
│   │   └── crud_booking.py           # Запросы по бронированиям и вычисление лимита
│   │
│   └── api/                          # HTTP эндпоинты (роуты)
│       ├── __init__.py
│       ├── deps.py                   # Зависимости FastAPI (get_db, get_current_user, проверка ролей)
│       └── v1/                       # Версионирование API (v1)
│           ├── __init__.py
│           ├── api.py                # Сборка всех роутеров v1 в один
│           └── endpoints/            # Конкретные контроллеры
│               ├── __init__.py
│               ├── auth.py           # /login, /register
│               ├── users.py          # Управление пользователями
│               ├── horses.py         # CRUD для лошадей (защищен ролями)
│               ├── services.py       # CRUD для услуг
│               └── bookings.py       # Создание записей и просмотр расписания
│
├── alembic/                          # Создастся позже командой: alembic init -t async alembic
│   ├── env.py
│   └── versions/
│
└── tests/                            # Автоматические тесты (Pytest)
    ├── __init__.py
    ├── conftest.py                   # Фикстуры: тестовая БД, тестовый клиент FastAPI
    ├── test_users.py                 # Тесты авторизации и прав доступа
    └── test_limits.py                # Тесты расчета лимита времени у лошадей
```

---

## 📋 Чек-лист для ручного создания

### 1. Корень проекта
- [ ] `.env`
- [ ] `.env.example`
- [ ] `.gitignore`
- [ ] `Dockerfile`
- [ ] `docker-compose.yml`
- [ ] `requirements.txt`

### 2. Пакет `app/`
- [ ] `app/__init__.py`
- [ ] `app/main.py`
- [ ] `app/config.py`
- [ ] `app/database.py`

### 3. Пакет `app/core/`
- [ ] `app/core/__init__.py`
- [ ] `app/core/security.py`

### 4. Пакет `app/models/`
- [ ] `app/models/__init__.py`
- [ ] `app/models/user.py`
- [ ] `app/models/horse.py`
- [ ] `app/models/service.py`
- [ ] `app/models/booking.py`

### 5. Пакет `app/schemas/`
- [ ] `app/schemas/__init__.py`
- [ ] `app/schemas/user.py`
- [ ] `app/schemas/horse.py`
- [ ] `app/schemas/service.py`
- [ ] `app/schemas/booking.py`

### 6. Пакет `app/crud/`
- [ ] `app/crud/__init__.py`
- [ ] `app/crud/crud_user.py`
- [ ] `app/crud/crud_horse.py`
- [ ] `app/crud/crud_service.py`
- [ ] `app/crud/crud_booking.py`

### 7. Пакет `app/api/`
- [ ] `app/api/__init__.py`
- [ ] `app/api/deps.py`
- [ ] `app/api/v1/__init__.py`
- [ ] `app/api/v1/api.py`
- [ ] `app/api/v1/endpoints/__init__.py`
- [ ] `app/api/v1/endpoints/auth.py`
- [ ] `app/api/v1/endpoints/users.py`
- [ ] `app/api/v1/endpoints/horses.py`
- [ ] `app/api/v1/endpoints/services.py`
- [ ] `app/api/v1/endpoints/bookings.py`

### 8. Пакет `tests/`
- [ ] `tests/__init__.py`
- [ ] `tests/conftest.py`
- [ ] `tests/test_users.py`
- [ ] `tests/test_limits.py`
