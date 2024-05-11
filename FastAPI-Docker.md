## Proyecto de FastApi   

<p align="center"><img src="./img/fastapi.png" alt="fastapi" height="100%" width="100%"/></p>

- **Paso 1:**  Crear Carpeta del Proyecto. 
my_first_API
______________________________
- **Paso 2:**  Crea un entorno virtual.
  
>[!NOTE]
>En la terminal de Visual estudio Code:

Terminal>
``` 
python -m venv venv
```			
>("-m", se refiere a que se instalará módulo de python, "venv" nombre del entorno virtual, de la siglas Virtual Enviroment)
>
>"Notar que se crea una carpeta en el directorio en el que nos encontramos."
______________________________
- **Paso 3:**  Activar entorno virtual.

En Windows:

Terminal>
```
venv/Scripts/activate
```
>"Notar que en la línea de comando ahora aparece, previa a la ruta la palabre (venv) PS C:\Users\my_first_API>

En Linux:
``` 
source venv/bin/activate
 ```

_______________________________
- **Paso 4:**  Instalar FastAPI
Terminal>
```
 pip install fastapi
```
________________________________________________
- **Paso 5:**  Instalar el módulo de ejcución de FastAPI
Terminal>
```
 pip install uvicorn
```
_____________________________________________________________
- **Paso 6:**  Crar el archivo para crer el código para Ejecutar API.

main.py
_________________________________________________________
- **Paso 7:**  Dentro del arcchivo importar el módulo de FastAPI
 ```
from fastapi import FastAPI
```

___________________________________________________________
- **Paso 8:** Se crea una instancia de FastAPI.
```
 app = FastAPI()
```
_________________________________
- **Paso 9:** Crear el primer endpoint:
```
@app.get('/')
  def message():
      return "Hello-World"
```
_______________________________
- **Paso 10:** Para correr en la API:

Terminal>

```
uvicorn main:app --reload
```		
>(Por defecto la aplicación se abre en el puerto 8000, para cambiar el puerto se añade la Bandera --port 5000)

```
uvicorn main:app --reload --port 5000
```

```
uvicorn main:app --reload --port 5000 --host 0.0.0.0
```

>(Ya la app estaría accesible a la red, se accede desde cualquier dispositivo con la ipmaquina:5000)
______________________________
- **Paso 11:** Para salir de la API:
Terminal:
>Control + C
Terminal> deactivate

							PARTE 2 (Documentación Api)
							---------------------------
________________________________________________________
- **Paso 1:** Acceder a la documentación automátca con Swagger.
Con la API levantada, (Ver Parte 1, paso 10)

Navegador>
```
ipmaquina:5000/docs
```

>[!NOTe]
>"Notar que se accede a una interfaz web que permite ver y acceder a nuestro endpoint"
________________________________________________________________
- **Paso 2:** Modificar el título de la documentación.
Dirigirse al Script que crea la API > main.py
Justo debajo luego de crear la instancia de FastAPI()
```
app.title = "My First API"
```
_____________________________
- **Paso 3:** Modificar la versión. 
```
app.version = "Basic 0.0.1"
```
___________________________________________
- **Paso 4:** Modificar la etiqueta del endpoint.
```
@app.get('/', tags=['home')
```
>("tags=['home'] se refiere al nombre que queremos usar, se debe pasar en una lista)
____________________________________________________________
- **Paso 5:** Uso de docstring para explicar el uso de la función.
Se agrega después de declarar la función antes del código agregar la descripción de lo que hace la función.

```
 def message():
    """Devuelve el mensaje de 'Hello Word'"""
    return "Hello World!"
```
 
							PARTE 3 ()
							---------------------------

## Llevar Fast API a Docker y luego hacer deployment.

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
pip install fastapi uvicorn
``````
- **Paso 4:** Crear una carpeta en la misma jerarquía, que la del entorno virtual de python. En este caso la llame "app"
``````
mkdir app
``````
- **Paso 5:** Ingresar a la carpeta creada
``````
cd app
``````
- **Paso 6:** Crear los archivos main.py y __init__.py, agregale el código que le da vida a tu API, tus módulos, agrega los archivos et...

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

