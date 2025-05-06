FROM python:3.11-slim

# Instala dependências e cria um usuário não-root
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && groupadd -r django && useradd -r -g django django \
    && mkdir /app && chown django:django /app \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia os arquivos com as permissões corretas
COPY --chown=django:django requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY --chown=django:django . .

USER django

ENV PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=mini_twitter.settings

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]