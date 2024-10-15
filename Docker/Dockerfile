# Descargar la imagen de ubuntu 
FROM ubuntu:22.04

# Actualizar la lista de actualizaciones  
RUN apt-get update

# Actualizar la imagen 
RUN apt-get upgrade -y

# Instalar las herramientas
RUN apt-get install python3 -y

# Copiar la carpeta webapp
COPY ./webapp /home/webapp

# Establecer el directorio de trabajo
WORKDIR /home/webapp

# Instalar pip
RUN apt-get install python3-pip -y

# Instalar las librerias
RUN pip install -r requirements.txt

# Abrir el puerto 8080
EXPOSE 8080 

# Ejecutar la aplicacion web
CMD [ "python3", "app.py"]