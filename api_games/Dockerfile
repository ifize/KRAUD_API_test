# Используйте официальный образ Python как базовый
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы с зависимостями в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в рабочую директорию
COPY . .

# Устанавливаем порт для работы приложения
EXPOSE 8000

# Запускаем приложение
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:8000", "api_games.wsgi:application"]
