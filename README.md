# 🚀 Магазин Мерча 

Это сервис для внутреннего магазина мерча в Авито, где сотрудники могут обмениваться монетками и приобретать товары. Проект реализован с использованием **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Docker** и **Poetry**.
Также реализовано покрытие бизнес сценариев юнит-тестами.  Общее тестовое покрытие проекта составляет 74%. Это можно проверить с помощью команды в терминале:
```bash
pytest --cov=avito --cov-report=term-missing
```
Чтобы запустить приложение напишите в терминале, заранее установив виртуальное окружение и все зависимости из Poetry файлов:
```bash
uvicorn main:main_app --host 0.0.0.0 --port 8080 --reload
```

---

## 🎨 Функционал
- Регистрация и авторизация пользователей с использованием **JWT**.
- Автоматическое создание пользователя при первой авторизации.
- Перевод монеток между сотрудниками.
- Покупка мерча (10 видов товаров с бесконечным запасом).
- Просмотр купленного мерча.
- История перемещений монеток:
  - Кто переводил монетки пользователю.
  - Кому пользователь переводил монетки.
- Защита от отрицательного баланса монеток.

---

## 💻 Технологии
- **FastAPI** — для создания REST API.
- **PostgreSQL** — в качестве основной базы данных.
- **SQLAlchemy** — для работы с БД.
- **FastAPI Users** — для аутентификации и авторизации.
- **Poetry** — для управления зависимостями.
- **Docker и Docker Compose** — для контейнеризации и запуска приложения.
- **Pytest** — для юнит-тестирования.

---

## 🚀 Установка и запуск

### 📦 С использованием Docker Compose

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/ribondareva/Test.git
cd Test
```
2. **Создайте файл .env в корневой директории (содержимое по подобию .env.template)**
3. **Запустите проект:**
```bash
docker-compose up --build
```
4. **Приложение будет доступно по адресу:**
```bash
http://localhost:8080
```
5. **Документация API (Swagger UI):**
```bash
http://localhost:8080/docs
```
### 📦 С использованием Dockerfile
Если хотите собрать образ и запустить контейнер вручную.
Находясь в корневой директории проекта:
1. **Соберите образ:**
```bash
docker build -t avito .
```
2. **Запустите контейнер:**
```bash
docker run -d --name avito -p 8080:8080 --env-file ./avito/.env avito
```
