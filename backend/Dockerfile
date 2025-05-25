
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

# Comando para manter o container em execução (sem executar comandos adicionais)
CMD ["tail", "-f", "/dev/null"]