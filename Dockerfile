# Utiliza una imagen precreada de Python 3.10
FROM python:3.10-slim

# El directorio donde trabajar
WORKDIR /app

# Copia el script del lanzador de datos en el script y el fichero de requirements 
COPY lanzamiento_dados.py .
COPY requirements.txt .

# Ejecutamos la instalacion de dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta el script cuando se inicie el contenedor queremos permitir la entrada de parametros
ENTRYPOINT ["python", "lanzamiento_dados.py"]

