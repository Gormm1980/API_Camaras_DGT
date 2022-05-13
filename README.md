# Configura un entorno virtual

Primero debes configurar el ambiente de trabajo. Primero instala y configura virtualenv, si ya lo tienes instalado ****puedes ejecutar lo siguiente:

 Crear el entorno virtual
- virtualenv venv

#Activar el ambiente virtual
- source venv/bin/activate

2. Instalar las frameworks / librerías

Recordemos que para realizar instalación de cualquier librería en Python, podemos hacerlo mediante el comando pip install <LIBRERIA> en este caso vamos a instalar las siguientes librerías

 - pip install django djangorestframework djangorestframework-simplejwt 

 - pip install django-model-utils

# Opcional
También podemos hacerlo creando un archivo llamado  requirements.txt  con las librerías que deseemos usar:

Django==3.0.8
 
djangorestframework==3.11.0
 
djangorestframework-simplejwt==4.4.0
 
django-model-utils==4.0.0

a continuación ejecutar el siguiente comando para instalar todas las librerías:

- pip install -r requirements.txt

 si os da el error: ERROR: Could not open requirements file: [Errno 2] No existe el archivo o el directorio: 'requirements.txt'
Tendreis que ejecutar el siguiente script en la terminal antes de instalar el requirements.txt

- pip freeze > requirements.txt


MUY IMPORTANTE INSTALAR PILLOW PARA TRABAJAR CON IMAGENES

- pip install Pillow

 El siguiente paso es crear un nuevo proyecto de Django


- django-admin startproject "nombre del proyecto"

Podemos asegurarnos que todo funcione hasta aquí. Puedes probar la ejecución del servidor Django con el siguiente comando:

- python manage.py runserver

# Crear aplicación

 Instalación y configuración de Django REST Framework

- pip install djangorestframework

 Para crar una migracion
 
- python manage.py makemigrations

Para ejecutar todas las migraciones
 
- python manage.py migrate

 Instalar psycopg2
 
- pip install psycopg2-binary
 
 Muy importante crear un super usuario para acceder al admin de Django.

- python3 manage.py createsuperuser

Después de instalar el framework debemos realizar la siguiente configuración, en el archivo settings.py vamos a agregar la aplicación rest_framework en la sección INSTALLED_APPS

INSTALLED_APPS = [
    ...
    'rest_framework',
]
