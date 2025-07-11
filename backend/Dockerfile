FROM python:3.11

# directorio
WORKDIR /app

# copiar archivos
COPY ./app /app/app

# instalar dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# exponer el puerto
CMD ["uvicorn", "app.main:app", "--host", "0.0.0", "--port", "8000", "--reload"]