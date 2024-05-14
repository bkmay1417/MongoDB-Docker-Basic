## Llevar Fast API a Docker y luego hacer deployment.

<p align="center"><img src="./img/docker.png" alt="docker"  height="100%" width="100%" /></p>

- **Paso 1:** Lo primero que vamos a hacer es crear un entorno virtual de python. 
``````
python -m venv env
``````
- **Paso 2:** Activar el entorno virtual de python
``````
.\env\Scripts\activate
``````
- **Paso 3:** Luego lo ideal instalar en linea de comando Fast API
``````
pip install yfinance pandas pymongo fastapi uvicorn
``````
- **Paso 4:** Crear una carpeta en la misma jerarquía, que la del entorno virtual de python. En este caso la llame "app"
``````
mkdir app
``````
- **Paso 5:** Ingresar a la carpeta creada
``````
cd app
``````
- **Paso 6:** Crear los archivos main.py(el del punto anterior) y __init__.py, agregale el código que le da vida a tu API, tus módulos, agrega los archivos et...

- **Paso 7:** Al finalizar tu application e instalar las dependencias, se debe guardar todos los módulos y versiones usadas en un archivo requirements.txt
``````
pip freeze > requirements.txt
``````
- **Paso 8:** Luego crea el archivo Dockerfile aquí un ejemplo basado en la documentación de FastAPI
``````
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
``````
- **Paso 9:** Luego asegurate de tener corriendo docker para construir la imagen de tu aplicación.
>[!NOTE]
>Este paso se ejecuta en ubuntu server

``````
docker build -t myapp .
``````

>[!NOTE]
>Demora un poco en crearse la imagen.

- **Paso 10:** En este punto asegúrate de tener una cuenta en [Dockerhub](https://hub.docker.com/) con los datos de tu cuenta te toca inciar sesión desde la línea de comando usando. 
``````
docker login
``````
- **Paso 11:** Luego de ingresar debes indicar el nombre de tu imagen asociado a tu usuario.
``````
docker tag myapp usuario/myapp
``````
- **Paso 12:** El siguiente paso será cargar la imagen a tu repo de docker hub.
``````
docker push timcepeda/myapp
``````
- **Paso 13:** Finalizado este paso es momento de ir a [render](https://render.com/) para deployar tu imagen de forma rápida. 

- Crea una cuenta en render
- Le das en crear un nuevo servicio web, en este caso usamos la versión free. 
- Indicas que es desde una imagen existente
- agrega la ruta de tu imagen como pista, sería usuario/myapp:latest
- Espera mientras se realiza el deployment

Al finalizar te pasará la url desde dónde puedes acceder a tu API. El resultado de este ejemplo lo puedes consumir [aquí](https://myapp-latest-qdyi.onrender.com) 

[Anterior](./yahoo-finance-mongodb.md)
[Back to Main README](./README.md)
