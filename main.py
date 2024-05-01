import yfinance as yf
from pymongo import MongoClient
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.param_functions import Path
from datetime import datetime
# Establecer la conexión a MongoDB
client = MongoClient('172.21.0.2', 27017)  # Por defecto, MongoDB corre en el puerto 27017 en localhost y la ip es la de la maquina virtual
lista_de_empresas = []
fecha = '2023-12-31'
tickers = ['TSLA', 'NFLX', 'META', 'AMZN', 'GOOG']
i = 1
# Recopilar datos de las empresas
for nombre_empresa in tickers:
    empresa = yf.Ticker(nombre_empresa)
    info = empresa.info
    dato = empresa.financials
    ceo_name = info.get("companyOfficers", [{}])[0].get("name", "No disponible")
    edad = info.get("companyOfficers", [{}])[1].get("age", "No disponible")
    # Crear el diccionario con los datos deseados
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
    i += 1
    lista_de_empresas.append(empresa_datos)
#print(lista_de_empresas)
# Seleccionar una base de datos (o "crear" una nueva al insertar datos)
db = client['finance']  # "Crear" una nueva base de datos llamada 
# Insertar un documento en una colección
collection = db['datos']  # "Crear" una colección llamada "mi_coleccion" dentro de la nueva base de datos
collection.insert_many(lista_de_empresas)
# Crear una instancia de FastAPI
app = FastAPI()
app.title = "My First API"
app.version = "Basic 0.0.1"
@app.get('/', tags=['home'])
def message():
    """Devuelve el mensaje de 'Hello Word' con enlace a lista de empresas"""
    
    return HTMLResponse('<h1>Hello World</h1><p><a href="/lista_de_empresas">Ver lista de empresas</a></p>')

@app.get("/lista_de_empresas", response_class=HTMLResponse)  # Corregir la ruta para mostrar la lista de empresas
async def read_items(request: Request):
    items_html = ""
    for empresa in lista_de_empresas:
        items_html += f"<h2>Empresa {empresa['Nombre de la empresa'],empresa['id']}</h2>"
        items_html += "<ul>"
        for key, value in empresa.items():
            items_html += f"<li><strong>{key}:</strong> {value}</li>"
        items_html += "</ul>"
    # Corrección: Corregir la estructura del HTML y el enlace
    html_content = f"<html><head><title>Lista de Empresas</title></head><body><a href='/'>Volver a la página de inicio</a>{items_html}</body></html>"
    return HTMLResponse(content=html_content, status_code=200)


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

