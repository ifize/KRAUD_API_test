# API для статистики игроков в онлайн-играх

API для работы со статистикой игроков в онлайн-играх, содержащее информацию о игроках, играх и статистике игр.

## Используемые технологии
* Django (Python)
* PostgreSQL (через Railway)
* Nginx
* Docker и Docker Compose

## Содержание

- [Установка](#установка)
- [Запуск с использованием Docker](#запуск-с-использованием-docker)
- [Эндпоинты](#эндпоинты)
  - [Создание игрока](#создание-игрока)
  - [Создание категории](#создание-категории)
  - [Создание онлайн-игры](#создание-онлайн-игры)
  - [Получение списка игроков](#получение-списка-игроков)
  - [Получение списка категорий](#получение-списка-категорий)
  - [Получение списка игр](#получение-списка-игр)
  - [Получение статистики](#получение-статистики)
  - [Обновление статистики](#обновление-статистики)
  - [Топ-5 игроков по времени](#топ-5-игроков-по-времени)
  - [Получение списка игр пользователя](#получение-списка-игр-пользователя)
- [Todo](#todo)

## Установка

1. Клонируйте репозиторий:

```bash
git clone git@github.com:ifize/KRAUD_API_test.git
```

2. Перейдите в каталог проекта и установите все необходимые зависимости:

```bash
cd api_games
pip install -r requirements.txt
```
3. Создайте файл .env в корне проекта со следующим содержимым (замените значения на свои):
```makefile
DJANGO_SECRET_KEY=your_secret_key
```
4. Запустите сервер разработки Django:

```bash
python manage.py runserver
```
Сервер будет доступен по адресу http://127.0.0.1:8000/.

## Запуск с использованием Docker

1. Убедитесь, что у вас установлен Docker и Docker Compose.

2. В каталоге проекта выполните следующую команду:

```bash
docker-compose up
```

Сервер будет доступен по адресу http://localhost/.

## Эндпоинты
Все URL для эндпоинтов начинаются с http://localhost:80/api/ или http://127.0.0.1:8000/api/ в зависимости от способа запуска.
### Создание игрока

* URL: `/players/create/`
* Метод: `POST`
* Тело запроса: JSON с полями `name` и `age`
* Ответ: JSON с полями `status` и `player_id`

Пример ответа:
```json
{
  "status": "success",
  "player_id": 1
}
```

### Создание категории

* URL: `/categories/create/`
* Метод: `POST`
* Тело запроса: JSON с полями `name` и `description`
* Ответ: JSON с полями `status` и `category_id`

Пример ответа:
```json
{
  "status": "success",
  "category_id": 1
}
```

### Создание онлайн-игры

* URL: `/games/create/`
* Метод: `POST`
* Тело запроса: JSON с полями `name` и `description` и массивом `categories` (список ID категорий)
* Ответ: JSON с полями `status` и `game_id`

Пример ответа:
```json
{
  "status": "success",
  "category_id": 1
}
```

### Получение списка игроков

* URL: `/players/`
* Метод: `GET`
* Ответ: JSON с массивом `players`, содержащим объекты с полями `id`, `name`, `age`

Пример ответа:
```json
{
  "players": [
    {
      "id": 1,
      "name": "Игрок 1",
      "age": 25
    },
    {
      "id": 2,
      "name": "Игрок 2",
      "age": 30
    }
  ]
}
```

### Получение списка категорий

* URL: `/categories/`
* Метод: `GET`
* Ответ: JSON с массивом `categories`, содержащим объекты с полями `id`, `name`, `description`

Пример ответа:
```json
{
  "categories": [
    {
      "id": 1,
      "name": "Категория 1",
      "description": "Описание категории 1"
    },
    {
      "id": 2,
      "name": "Категория 2",
      "description": "Описание категории 2"
    }
  ]
}
```

### Получение списка игр

* URL: `/games/`
* Метод: `GET`
* Ответ: JSON с массивом `games`, содержащим объекты с полями `id`, `name`, `description`

Пример ответа:
```json
{
  "games": [
    {
      "id": 1,
      "name": "Игра 1",
      "description": "Описание игры 1"
    },
    {
      "id": 2,
      "name": "Игра 2",
      "description": "Описание игры 2"
    }
  ]
}
```

### Получение статистики

* URL: `/statistics/`
* Метод: `GET`
* Ответ: JSON с массивом `statistic`, содержащим объекты с полями id, `player_id`, `score`, `time_played`, `game_id`

Пример ответа:
```json
{
  "statistic": [
    {
      "id": 1,
      "player_id": 1,
      "score": 100,
      "time_played": 120,
      "game_id": 1
    },
    {
      "id": 2,
      "player_id": 2,
      "score": 200,
      "time_played": 240,
      "game_id": 1
    }
  ]
}
```

### Обновление статистики

* URL: `/statistics/update/`
* Метод: `PUT`
* Тело запроса: JSON с полями `player_id`, `game_id`, `score`, `time_played`
* Ответ: JSON с полем `status`

Пример ответа:
```json
{
  "status": "success"
}
```

### Топ-5 игроков по времени

* URL: `/top_players/`
* Метод: `GET`
* Ответ: JSON с массивом `top_players`, содержащим объекты с полями `player__name` и `total_time_played`

Пример ответа:
```json
{
  "top_players": [
    {
      "player__name": "Игрок 1",
      "total_time_played": 350
    },
    {
      "player__name": "Игрок 2",
      "total_time_played": 200
    }
  ]
}
```

### Получение списка игр пользователя

* URL: `/user_games/<int:player_id>/`
* Метод: `GET`
* Ответ: JSON с массивом `games`, содержащим объекты с полями `id`, `name`, `description`

Пример ответа:
```json
{
  "games": [
    {
      "id": 1,
      "name": "Игра 1",
      "description": "Описание игры 1"
    },
    {
      "id": 2,
      "name": "Игра 2",
      "description": "Описание игры 2"
    }
  ]
}
```

## ToDo
* Реализовать аутентификацию и авторизацию пользователей.
* Добавить пагинацию для API-запросов.
* Добавить фильтрацию и сортировку для списка игр и игроков.
* Реализовать возможность добавления изображений для игр и категорий.
* Добавить тесты для API-эндпоинтов.
* Оптимизировать запросы к базе данных.
* Добавить поддержку других баз данных (например, MySQL или SQLite).
* Реализовать кэширование для улучшения производительности.
* Развернуть проект на удаленном сервере (например, на Heroku или AWS).
* Разработать веб-интерфейс для работы с API (React, Angular, Vue.js и т. д.).