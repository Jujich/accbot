# Используем официальный образ Python
FROM python:3.11-slim as builder

# Устанавливаем зависимости системы
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev

# Создаем виртуальное окружение
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Финальный образ
FROM python:3.11-slim

# Копируем виртуальное окружение из builder
COPY --from=builder /opt/venv /opt/venv

# Устанавливаем переменные окружения
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Создаем и переходим в рабочую директорию
WORKDIR /app

# Копируем исходный код
COPY . .

# Команда для запуска приложения
CMD ["python", "main.py"]