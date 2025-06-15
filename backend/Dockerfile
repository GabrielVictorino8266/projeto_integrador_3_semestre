
FROM python:3.11

WORKDIR /app

# Copiar requirements.txt
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código fonte do projeto
COPY . .

# Expor a porta 8000
EXPOSE 8000

# Comando para executar o Django na porta 8000
# CMD ["sh", "-c", "python api/manage.py migrate_mongo && tail -f /dev/null"]

# Comando para manter o container em execução (sem executar comandos adicionais)
# CMD ["sh", "-c", "python api/manage.py migrate_mongo && python api/manage.py runserver 0.0.0.0:8000"]

# descomentar para rodar em modo de desenvolvimento