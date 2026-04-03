# Image base para icialização do projeto
FROM python:3.14-slim

#Previne criação de arquivos .pyc e buffer de output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala depêndencias do sistema necessárias para psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

#Copia e instala dependências Python PRIMEIRO (Cache de layers)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copia o código
COPY . .

#Cria diretório de logs
RUN mkdir -p /app/logs

# Usuário não-root
RUN useradd -m certadmin && chown -R certadmin:certadmin /app
USER certadmin

EXPOSE 8000


#Gunicorn com workers otmizados para 1 core
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "certpremium.wsgi:application"]


