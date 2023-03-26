# Используйте официальный образ Python
FROM python:3.9

# Установите рабочую директорию
WORKDIR /code

# Установите зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте все файлы проекта
COPY . .

# Соберите статические файлы
RUN python manage.py collectstatic --noinput
