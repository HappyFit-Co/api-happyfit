# Dockerfile
FROM python:3.8-slim

# Definindo o diretório de trabalho no container
WORKDIR /app

# Copiando o diretório do código-fonte para o diretório de trabalho
COPY . .

# Instalando as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expondo a porta em que o aplicativo irá escutar
EXPOSE 8080

# Comando para executar o aplicativo
CMD ["python", "server.py"]
