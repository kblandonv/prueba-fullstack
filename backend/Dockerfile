FROM python:3.11

WORKDIR backend/app

# 1) Copia e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) Copia el código de tu aplicación
COPY app/ ./app

# 3) Documenta el puerto que usarás (opcional)
EXPOSE 8000

# 4) Comando que arranca FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
