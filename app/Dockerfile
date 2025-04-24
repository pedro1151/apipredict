#FROM python:3.9-alpine3.12
FROM python:3.9-slim
WORKDIR /app

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Instalar librerías necesarias para compilar paquetes como cryptography
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libxml2-dev \
    libxslt-dev \
    cargo \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt


CMD ["flask", "run"]