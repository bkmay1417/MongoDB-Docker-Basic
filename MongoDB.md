# Instalación de MongoDB
<p align="center"><img src="./img/mongodb.png" alt="mongodb"  /></p>

Para instalar MongoDB, sigue los siguientes pasos en la línea de comando:
____________________________________________
- **Paso 1:**  Crear el archivo docker-compose.yml
Primero, vamos a crear un directorio para organizar nuestro proyecto y dentro de él crearemos el archivo docker-compose.yml.

```
mkdir Mongo
```
```
cd Mongo
```
crear el archivo .yml
```
touch docker-compose.yml
```
____________________________________________
- **Paso 2:** Editar el archivo docker-compose.yml
Ahora, editaremos el archivo docker-compose.yml para configurar nuestro servicio de MongoDB. Asegúrate de reemplazar "user" y "pass" con el usuario y la contraseña deseados,al terminar de copiar aprtete un enter y ctr + d para grabar y continuar.
```
        version: '2.2'
        services:
          mongo:
            image: mongo:4.0.4
            restart: always
            container_name: monguito
            environment:
              - MONGODB_USER="user"
              - MONGODB_PASS="pass"
            volumes:
              - ./monguitodata:/data/db
              - ./monguitodata/log:/var/log/mongodb/
            ports:
              - "27017:27017"
 ```    
_____________________________________________________________
- **Paso 3:** Crear un script para ejecutar comandos en la terminal
Vamos a crear un script llamado mongo.sh que nos ayudará a automatizar algunas tareas.
```
touch mongo.sh
```
__________________________________
- **Paso 4:** Editar el archivo mongo.sh
A continuación, editaremos el archivo mongo.sh y agregaremos los comandos necesarios.

#Crear carpeta para volumen de mongo:
```
mkdir monguitodata && cd monguitodata; cd monguitodata || mkdir log
```
> mkdir monguitodata
> cd monguitodata
> mkdir log
> cd mongo

#Iniciar el contenedor

```
sudo docker-compose up -d
```
Mostrar mensaje
```
echo "Monguito se está iniciando..."
```
Entrar en el contenedor
```
sudo docker exec -it monguito bash
```
_________________________________________________________
- **Paso 5:** Asignar permisos de ejecución y ejecutar mongo.sh
Finalmente, asignaremos permisos de ejecución al script y lo ejecutaremos.
```
chmod u+x mongo.sh
```
```
./mongo.sh
```
_______________________________
- **Paso 6:** ¡Usar MongoDB a placer!
¡Listo! Ahora puedes utilizar MongoDB según tus necesidades.

Para realizar esto usamos los siguentes comando 

- sudo = permiso de super usario
- touch = crear un archivo
- car = edicion de un archivo
- mkdir= crear un directorio/carperta
- cd= moverse dentro de una carpeta
- chmod u+x = dar permisos de ejecucion
- sudo docker-compose up -d

## MongoDB-Docker-Basic
Proyecto basico de  mongodb con docker

			COMANDOS MONGO DB
_______________________
Mostrar Bases de datos:
```
show dbs
```
______________________________________
Crear o ubicarse en uns base de datos:
```
use databasename
```
_______________________________________
Saber que base de datos estamos usando:
```
db
```
________________
Crear colección:
``` 
db.createCollection('nameCollection')
```
{"Clave": "Valor"}

________________
Mostrar el contenido de una colección:
```
use database
```
```
db.dropDatabase()
```
```
use tabla;
```
```
showCollections;
```
```
db.tabla.find();
```
[Anterior](./Pre-requisitos.md)
[Siguiente](./yahoo-finance-mongodb.md)
[Back to Main README](./README.md)
