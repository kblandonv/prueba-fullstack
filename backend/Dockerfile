FROM python:3.11

# 1) Define el directorio de trabajo
WORKDIR /app

# 2) Copia e instala las dependencias primero
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# 3) Copia TODO el código de tu backend
COPY . /app

# 4) Expón el puerto (documentación)
EXPOSE 8000

# 5) Manda a ejecutar tu servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
