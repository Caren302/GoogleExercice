# GoogleExercice

## Instalar paquetes

## Visualizar vista de paquetes

Para instalar la lista de paquetes se utiliza el siguiente comando:

''' bash
    $ pip freeze
'''

## Instalar todos los paquetes necesarios

Para instalar todos los paquetes necesarios se crea una lista en el archivo requirements.txt y se ejecuta el siguiente comando:

''' bash
    $ pip3 install -r requirements.txt
'''

## Generar arcivo requirements.txt



## Ejecutar la aplicacion web

En este ejemplo se instala (web.py) (https://webpy.org), se utiliza el coidgo de ejemplo y se ejecuta

''' bash
    $ python3 app.py
'''

## Actualizar el repositorio 

Despues de verificar que funciona la aplicación

''' bash
    git add .
    git commit -m "CREATED hola mundo"
    git push -u origin main
'''


docker build -t image:tag .

docker run 

///////////////////////////////////////////////////////////////

# Descargar la imagen de Docker
FROM ubuntu:22.04

# Actualizar la imagen
RUN apt-get update && apt-get upgrade -y

# Instalar herramientas necesarias
RUN apt-get install -y python3 python3-pip

# Copiar la carpeta
COPY ./app /home/app

# Establecer directorio de trabajo
WORKDIR /home/app

# Instalar librerías Python
RUN pip3 install -r requirements.txt

# Abrir el puerto 8080
EXPOSE 8080

# Ejecutar la aplicación
CMD [ "python3", "app.py" ]