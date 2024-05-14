## Agregar Fast API a nuestro proyecto.
<p align="center"><img src="./img/drawio.png" alt="drawio" height="60%" width="60%"/></p>

### Buscamos hacer algo asi 
## Descripción

Este proyecto mejoraremos el proyecto anterior agregando un forma de visualizar los datos utiliza la biblioteca `fastapi` para poder generan una pagina con los datos financieros de varias empresas y los almacena en una base de datos MongoDB.

## Instalación

Para instalar las dependencias del proyecto, asegúrate de tener `yfinance`,`fastapi`,`pandas` y `pymongo` instalados en tu entorno Python. Puedes instalarlos utilizando pip:

```
pip install yfinance pandas pymongo fastapi uvicorn
```

## Uso
Para ejecutar el código, simplemente ejecuta el script main.py. Asegúrate de tener una instancia de MongoDB en ejecución y especifica la dirección IP y el puerto correctos en la variable client.

```
python main.py
```
Contribución
Si deseas contribuir al proyecto, puedes abrir issues para informar sobre problemas o sugerir mejoras. También puedes enviar pull requests con cambios propuestos.

Enlaces
- [Documentación de FastAPI](https://fastapi.tiangolo.com/) 

## Documentacion de las modificaciones al codigo previo

### 1. Importaciones de bibliotecas (ACTUALIZADO CON MAS LIBRERIAS)
```
# Importar las bibliotecas necesarias
import yfinance as yf  # Para obtener datos financieros
import pandas as pd  # Para manejar datos de forma tabular
from datetime import datetime  # Para manejar fechas
from pymongo import MongoClient  # Para conectarse a MongoDB

#NUEVO
# Importar las bibliotecas necesarias para FastAPI
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.param_functions import Path
```
### 2. Establecer la conexión a MongoDB (SIN CAMBIOS)

```
# Establecer la conexión a MongoDB
client = MongoClient('192.168.0.21', 27017)  # Conectarse a MongoDB en la dirección especificada y en el puerto 27017

```
### 3. Obtención de datos financieros de empresas y construcción de diccionarios (CAMBIOS MENORES)
```
# Definir una lista para almacenar los datos de las empresas
lista_de_empresas = []
# Definir una fecha específica para obtener los datos financieros
fecha = '2023-12-31'
# Lista de símbolos de empresas para obtener datos
tickers = ['TSLA', 'NFLX', 'META', 'AMZN', 'GOOG']

#NUEVO
# Inicializar un contador para asignar un ID único a cada empresa
i = 1

# Iterar sobre cada símbolo de empresa en la lista

for nombre_empresa in tickers:
    # Obtener datos financieros de la empresa usando yfinance
    empresa = yf.Ticker(nombre_empresa)
    info = empresa.info
    dato = empresa.financials

    # Obtener información sobre el CEO y su edad
    ceo_name = info.get("companyOfficers", [{}])[0].get("name", "No disponible")
    edad = info.get("companyOfficers", [{}])[1].get("age", "No disponible")

    #MODIFICADO PARA TENER ID 
    # Crear un diccionario con los datos deseados de la empresa
    empresa_datos = {
        "id": i,
        "Nombre de la empresa": info.get("longName", "No disponible"),
        "Sector": info.get("sector", "No disponible"),
        "CEO": ceo_name,
        "Edad del CEO": edad,
        "Volumen promedio": info.get("averageVolume", "No disponible"),
        "Tax Rate For Calcs": dato[fecha]["Tax Rate For Calcs"],
        "Reconciled Depreciation ": dato[fecha]["Reconciled Depreciation"],
        "EBITDA ": dato[fecha]["EBITDA"],
        "Interest Expense": dato[fecha]["Interest Expense"],
        "Gross Profit": dato[fecha]["Gross Profit"]
    }
    
    # Incrementar el contador
    i += 1
    
    # Agregar los datos de la empresa a la lista
    lista_de_empresas.append(empresa_datos)
```

### 4. Conexión y almacenamiento de datos en MongoDB (SIN CAMBIOS)
```
# Seleccionar una base de datos (o "crear" una nueva al insertar datos)
db = client['finance']  # Seleccionar o crear una base de datos llamada 'finance'

# Insertar documentos en una colección
collection = db['datos']  # Seleccionar o crear una colección llamada 'datos' dentro de la base de datos 'finance'
collection.insert_many(lista_de_empresas)  # Insertar los datos de las empresas en la colección 'datos'
```
### 5. Crear una instancia de FastAPI (NUEVO SE UTLIZA UN POCO HTML)

```
app = FastAPI()
app.title = "My First API"
app.version = "Basic 1.0.0"

# Ruta para la página de inicio
@app.get('/', tags=['home'])
def message():
    """Devuelve el mensaje de 'Hello Word' con un enlace a la lista de empresas"""
    return HTMLResponse('<h1>Hello World</h1><p><a href="/lista_de_empresas">Ver lista de empresas</a></p>')

# Ruta para mostrar la lista de empresas
@app.get("/lista_de_empresas", response_class=HTMLResponse)
async def read_items(request: Request):
    """Devuelve una página HTML con la lista de empresas y sus detalles"""
    items_html = ""
    for empresa in lista_de_empresas:
        items_html += f"<h2>Empresa {empresa['Nombre de la empresa']}, ID: {empresa['id']}</h2>"
        items_html += "<ul>"
        for key, value in empresa.items():
            items_html += f"<li><strong>{key}:</strong> {value}</li>"
        items_html += "</ul>"
    html_content = f"<html><head><title>Lista de Empresas</title></head><body><a href='/'>Volver a la página de inicio</a>{items_html}</body></html>"
    return HTMLResponse(content=html_content, status_code=200)

# Ruta para obtener los detalles de una empresa por su ID
@app.get('/lista_de_empresas/{id}', tags=['lista_de_empresas'], response_class=HTMLResponse)
def get_empresa_by_id(id: int = Path(..., title="ID de la empresa a buscar")):
    """Devuelve los detalles de una empresa por su ID"""
    for empresa in lista_de_empresas:
        if empresa["id"] == id:
            # Construir HTML para los detalles de la empresa
            html_content = f"""
            <html>
                <head>
                    <title>Detalles de la Empresa</title>
                </head>
                <body>
                    <h1>Detalles de la Empresa</h1>
                    <h2>Empresa {empresa['Nombre de la empresa']} (ID: {empresa['id']})</h2>
                    <ul>
                        <li><strong>Sector:</strong> {empresa['Sector']}</li>
                        <li><strong>CEO:</strong> {empresa['CEO']}</li>
                        <li><strong>Edad del CEO:</strong> {empresa['Edad del CEO']}</li>
                        <li><strong>Volumen promedio:</strong> {empresa['Volumen promedio']}</li>
                        <li><strong>Tax Rate For Calcs:</strong> {empresa['Tax Rate For Calcs']}</li>
                        <li><strong>Reconciled Depreciation:</strong> {empresa['Reconciled Depreciation ']}</li>
                        <li><strong>EBITDA:</strong> {empresa['EBITDA ']}</li>
                        <li><strong>Interest Expense:</strong> {empresa['Interest Expense']}</li>
                        <li><strong>Gross Profit:</strong> {empresa['Gross Profit']}</li>
                    </ul>
                    <p><a href="/lista_de_empresas">Volver a la lista de empresas</a></p>
                </body>
            </html>
            """
            return HTMLResponse(content=html_content, status_code=200)
    # Si no se encuentra la empresa, retornar un error 404
    raise HTTPException(status_code=404, detail="Empresa no encontrada")
```
### Resultado final 
<p align="center"><img src="./img/Screenshot_73.png" alt="sce" height="60%" width="60%"/></p>

