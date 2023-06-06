# Используем базовый образ Python
FROM python:3.9-slim

# Указываем рабочую директорию
WORKDIR /model_api

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential python3-dev libffi-dev libssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем код в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r req.txt

# Запускаем сервер при запуске контейнера
CMD ["uvicorn", "model_api:app", "--host", "0.0.0.0", "--port", "8000"]