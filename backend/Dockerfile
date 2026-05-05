# Usamos una versión ligera de Python 3.11
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requisitos e instalamos las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código del backend
COPY . .

# Comando para ejecutar la aplicación al iniciar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]