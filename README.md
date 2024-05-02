<h1> Configuración de un Contenedor de MongoDB con Docker</h1>

<p align="center"><img src="./img/mongodb.png" alt="mongodb"  /></p>

<h2>Pre-requisitos 📋</h2>

En este proyecto se llevó a cabo en un entorno de desarrollo Windows. Se utilizó una máquina virtual alojada en VirtualBox con Ubuntu Server, debido a que Docker no es compatible directamente con Windows. En la máquina virtual se instaló Docker para la gestión de contenedores. Para establecer la conexión entre la máquina virtual y el sistema operativo original de Windows, se empleó PuTTY. Además, para simplificar la transferencia y gestión de archivos en Ubuntu, también se puede optar por utilizar WinSCP.Los links se proveen a continuacion

Paso 0.01 Descarga el virtual disk de Ubuntu Server desde el siguiente enlace: [Descargar Ubuntu Server](https://drive.google.com/file/d/1EsDIcfz-MVvPwOSmUb-x5FE612puBZnF/view) (2.15 gb)

<p><img src="./img/imangenlink.png" alt="imangenlink" width="75%" height="75%" /></p>

Paso 0.02 Descarga e instala VirtualBox desde: [Descargar VirtualBox](https://www.virtualbox.org/wiki/Downloads)

<p><img src="./img/Virtualbox0.1.png" alt="virtualbox0.1" width="75%" /></p>

Paso 0.03 Creamos una nueva maquina virtual

<p><img src="./img/Virtualbox0.png" alt="virtualbox0" width="75%" /></p>

Paso 0.04 La llamamos ubuntu

<p><img src="./img/Virtualbox1.png" alt="virtualbox1"    /></p>

Paso 0.05 Nos dirigimos a hard disk y ponemos utilizar un hard disk existente

<p><img src="./img/Virtualbox2.png" alt="virtualbox2"   /></p>

Paso 0.06 Elegimos el hardisk anteriormente descargado y finalizar

<p><img src="./img/Virtualbox3.png" alt="virtualbox3" width="75%"  /></p>

Paso 0.07 Luego configuramos los puestos de red

<p><img src="./img/Virtualbox4.png" alt="virtualbox4" /></p>

Paso 0.08 En el primer adaptador pones adaptador puente y en avanzado permitir todo

<p><img src="./img/Virtualbox5.png" alt="virtualbox5"   /></p>

Paso 0.09 En el segundo colocamos solo anfitrion y en avanzado permitir todo y guardamos 

<p><img src="./img/Virtualbox6.png" alt="virtualbox6" height="63%" width="63%"  /></p>

Paso 0.10 Iniciamos la maquina virtual 

> [!CAUTION]
> Este paso fallara si se tiene la virtualizacion de windows desactivada .
> En este [video](https://www.youtube.com/watch?v=Tl4kODRGtIc&ab_channel=LuisOvalle)  explican como revisar si esta activa y en caso de no estarlo como activarlo 

<p><img src="./img/Virtualbox6.1.png" alt="virtualbox6.1" width="75%"  /></p>

Paso 0.11 esperamos un poco y ingresamos el usuario  y comtraseña  (por defecto viene ubuntu de usuario y ubuntu de contraseña)

<p><img src="./img/Virtualbox7.png" alt="virtualbox7" width="75%"  /></p>

Paso 0.12 A continuacion obtenemos el ip de la maquina virtual

```
hostname -I
```

<p><img src="./img/Virtualbox8.png" alt="virtualbox8" width="75%"  /></p>

Paso 0.13 Descargamos e instalamos el putty : [Descargar putty](https://www.putty.org/)

<p><img src="./img/putty.png" alt="putty0"  width="75%" /></p>

Paso 0.14 Iniciamos el putty con la ip usuario y comtraseña de la maquina virtual

<p><img src="./img/putyy1.png" alt="putty1"   /></p>

Paso 0.15 Despues ingresamos el usuario y contraseña

<p><img src="./img/putty2.png" alt="putty2" height="63%" width="63%" /></p>

Paso 0.16 Opcional descargar e instalar winscp : [Descargar winscp](https://winscp.net/eng/download.php)

<p><img src="./img/winscp0.png" alt="winscp0" width="75%"  /></p>

Paso 0.17 Programa que nos permite editar y enviar archivos de una forma mas comoda se conecta igual que el putty con el ip de la maquina virtual

<p><img src="./img/winscp.png" alt="winscp" width="75%"  /></p>

<p align="right">(<a href="#readme-top">Volver al principio</a>)</p>


Instalación de MongoDB:
Para instalar MongoDB, sigue los siguientes pasos en la línea de comando:
____________________________________________
Paso 1: Crear el archivo docker-compose.yml
Primero, vamos a crear un directorio para organizar nuestro proyecto y dentro de él crearemos el archivo docker-compose.yml.

```
mkdir Mongo
```
```
cd Mongo
```

#touch = crear el archivo .yml
```
touch docker-compose.yml
```
____________________________________________
Paso 2: Editar el archivo docker-compose.yml
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
Paso 3: Crear un script para ejecutar comandos en la terminal
Vamos a crear un script llamado mongo.sh que nos ayudará a automatizar algunas tareas.
```
touch mongo.sh
```
__________________________________
Paso 4: Editar el archivo mongo.sh
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
#Mostrar mensaje
```
echo "Monguito se está iniciando..."
```
#Entrar en el contenedor
```
sudo docker exec -it monguito bash
```
_________________________________________________________
Paso 5: Asignar permisos de ejecución y ejecutar mongo.sh
Finalmente, asignaremos permisos de ejecución al script y lo ejecutaremos.
```
chmod u+x mongo.sh
```
```
./mongo.sh
```
_______________________________
Paso 6: ¡Usar MongoDB a placer!
¡Listo! Ahora puedes utilizar MongoDB según tus necesidades.



Para realizar esto usamos los siguentes comando 

#sudo = permiso de super usario
#touch = crear un archivo
#car = edicion de un archivo
#mkdir= crear un directorio/carperta
#cd= moverse dentro de una carpeta
#chmod u+x = dar permisos de ejecucion
#sudo docker-compose up -d











# MongoDB-Docker-Basic
protecto basico de  mongodb con docker

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

# Referencias

* 


## Desarrolladores

| [<img src="https://avatars.githubusercontent.com/u/163685041?v=4" width=115><br><sub>Michael Martinez</sub>](https://github.com/bkmay1417) |
| :---: |

Copyright (c) 2024 [Michael Martinez] yam8991@gmail.com
