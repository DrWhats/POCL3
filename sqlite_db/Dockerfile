# Используйте минимальный базовый образ
FROM alpine:latest

# Создайте директорию для хранения файла SQLite
RUN mkdir /database

# Копируйте ваш файл SQLite в созданную директорию
COPY db /database/

# Устанавливаем права на файл базы данных
RUN chmod 644 /database/db

# Экспортируйте директорию с файлом SQLite для использования в других контейнерах
VOLUME /database