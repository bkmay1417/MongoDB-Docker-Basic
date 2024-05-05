## Proyecto de FastApi   

<p align="center"><img src="./img/fastapi.png" alt="fastapi" height="100%" width="100%"/></p>

- Paso1- Crear Carpeta del Proyecto. 
my_first_API
______________________________
-  Paso2- Crea un entorno virtual. 
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
- Paso3- Activar entorno virtual.

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
- Paso4- Instalar FastAPI
Terminal>
```
 pip install fastapi
```
________________________________________________
- Paso5- Instalar el módulo de ejcución de FastAPI
Terminal>
```
 pip install uvicorn
```
_____________________________________________________________
- Paso6- Crar el archivo para crer el código para Ejecutar API.

main.py
_________________________________________________________
- Paso 7- Dentro del arcchivo importar el módulo de FastAPI
 ```
from fastapi import FastAPI
```

___________________________________________________________
- Paso 8- Se crea una instancia de FastAPI.
```
 app = FastAPI()
```
_________________________________
- Paso 9- Crear el primer endpoint:
```
@app.get('/')
  def message():
      return "Hello-World"
```
_______________________________
- Paso 10- Para correr en la API:

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
- Paso 11- Para salir de la API:
Terminal:
>Control + C
Terminal> deactivate

							PARTE 2 (Documentación Api)
							---------------------------
________________________________________________________
- Paso 1- Acceder a la documentación automátca con Swagger.
Con la API levantada, (Ver Parte 1, paso 10)

Navegador>
```
ipmaquina:5000/docs
```
>[!NOTA]
>"Notar que se accede a una interfaz web que permite ver y acceder a nuestro endpoint"
________________________________________________________________
- Paso 2- Modificar el título de la documentación.
Dirigirse al Script que crea la API > main.py
Justo debajo luego de crear la instancia de FastAPI()
```
app.title = "My First API"
```
_____________________________
- Paso 3- Modificar la versión. 
```
app.version = "Basic 0.0.1"
```
___________________________________________
- Paso 4- Modificar la etiqueta del endpoint.
```
@app.get('/', tags=['home')
```
>("tags=['home'] se refiere al nombre que queremos usar, se debe pasar en una lista)
____________________________________________________________
- Paso 5- Uso de docstring para explicar el uso de la función.
Se agrega después de declarar la función antes del código agregar la descripción de lo que hace la función.

```
 def message():
    """Devuelve el mensaje de 'Hello Word'"""
    return "Hello World!"
```
 
