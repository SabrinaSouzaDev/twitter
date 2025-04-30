# Docker/Dockerfile
FROM python:3.11-slim

# Configurações essenciais
ENV DJANGO_SETTINGS_MODULE=mini_twitter.settings

# Instala dependências de sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Cria e define o diretório de trabalho
RUN mkdir -p /app
WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
# Copia e instala dependências Python (otimizando cache)
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o projeto (contexto é o diretório onde docker-compose está)
COPY . .

# Porta do aplicativo
EXPOSE 8000

# Comando de produção (Gunicorn)
ENV DJANGO_SETTINGS_MODULE=mini_twitter.settings
CMD ["gunicorn", "mini_twitter.wsgi:application", "--bind", "0.0.0.0:8000"]