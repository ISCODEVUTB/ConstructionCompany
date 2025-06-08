# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código al contenedor
COPY src ./src

# Establece la variable de entorno PYTHONPATH
ENV PYTHONPATH=/app/src

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["uvicorn", "src.backend.app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]