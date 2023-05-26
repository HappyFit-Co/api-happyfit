# Estágio de compilação
FROM python:3.8-alpine as builder

WORKDIR /app

# Copie apenas os arquivos necessários para instalar as dependências
COPY requirements.txt .

# Instale as dependências de compilação
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir --prefix=/install -r requirements.txt

# Estágio de execução
FROM python:3.8-alpine

WORKDIR /app

# Copie o restante do projeto do estágio de compilação
COPY --from=builder /install /usr/local
COPY . .

# Exponha a porta em que o aplicativo irá escutar
EXPOSE ${PORT}

# Comando para executar o aplicativo
CMD ["python", "server.py"]
