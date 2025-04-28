# Usando a imagem oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo de requisitos para o container
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar todo o conteúdo do projeto para o container
COPY . .

# Definir a variável de ambiente DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=config.settings

# Expor a porta do aplicativo
EXPOSE 5000

# Comando para rodar o gunicorn e iniciar o Django
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:5000"]
