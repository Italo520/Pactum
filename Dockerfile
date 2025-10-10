# Usar uma imagem oficial do Python
FROM python:3.10-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto
COPY . /app/

# Criar diretório de logs
RUN mkdir -p /app/logs
# Expor a porta que o Gunicorn vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "Pactum.wsgi:application"]
