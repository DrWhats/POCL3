# Используйте официальный образ Python 3.9
FROM python:3.9-slim

# Задайте рабочую директорию
WORKDIR /flask_app

# Установите переменные окружения
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Обновите пакеты и установите зависимости
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential python3-dev libffi-dev libssl-dev curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Скопируйте файлы проекта
COPY req.txt req.txt

# Установите зависимости Python
RUN pip install --no-cache-dir -r req.txt

# Скопируйте оставшиеся файлы проекта
COPY . .

VOLUME /instance

# Экспонируйте порт для работы с приложением
EXPOSE 5000

# Запустите приложение Flask
CMD ["flask", "run", "--port=5000"]