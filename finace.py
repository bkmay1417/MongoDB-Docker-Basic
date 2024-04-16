import yfinance as yf
import pandas as pd
from datetime import datetime
import pymongo
from pymongo import MongoClient

# Establecer la conexión a MongoDB
client = MongoClient('192.168.0.21', 27017)  # Por defecto, MongoDB corre en el puerto 27017 en localhost y la ip es la de la maquina virtual

lista_de_empresas = []
fecha = '2023-12-31'
tickers = ['TSLA', 'NFLX', 'META', 'AMZN', 'GOOG']


for nombre_empresa  in tickers:
    empresa = yf.Ticker(nombre_empresa)
    info = empresa.info
    dato=empresa.financials
    ceo_name = info.get("companyOfficers", [{}])[0].get("name", "No disponible")
    edad=info.get("companyOfficers", [{}])[1].get("age", "No disponible")
    # Crear el diccionario con los datos deseados
    empresa_datos = {
        "Nombre de la empresa": info.get("longName", "No disponible"),
        "Sector": info.get("sector", "No disponible"),
        "CEO": ceo_name,
        "Edad del CEO": edad,
        "Volumen promedio": info.get("averageVolume", "No disponible"),
        "Tax Rate For Calcs":dato[fecha]["Tax Rate For Calcs"],
        "Reconciled Depreciation ":dato[fecha]["Reconciled Depreciation"],
        "EBITDA ":dato[fecha]["EBITDA"],
        "Interest Expense":dato[fecha]["Interest Expense"],
        "Gross Profit":dato[fecha]["Gross Profit"]
    }
    lista_de_empresas.append(empresa_datos)
print(lista_de_empresas)

# Seleccionar una base de datos (o "crear" una nueva al insertar datos)
db = client['finance']  # "Crear" una nueva base de datos llamada 

# Insertar un documento en una colección
collection = db['datos']  # "Crear" una colección llamada "mi_coleccion" dentro de la nueva base de datos
collection.insert_many(lista_de_empresas)
